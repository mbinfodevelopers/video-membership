import logging
from django.http import Http404, HttpResponse
from django.core.mail import send_mail
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from payment.models import Payment
from django.shortcuts import render
from order.models import Order, OrderItem, Cart
from django.contrib import messages
from django.conf import settings as mysettings


def go_to_gateway_view(request):

    # to get the total price of items in cart
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    if cart_items:
        for item in cart_items:
            total_price += item.course.price

    amount = total_price

    factory = bankfactories.BankFactory()
    try:
        bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)

        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url('/callback-gateway')

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        raise e


def callback_gateway_view(request):
    context = {}
    current_user = request.user
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)

    context['tracking_code'] = tracking_code

    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # to create payment object
    new_payment = Payment()
    new_payment.user = current_user
    new_payment.payment_number = bank_record.tracking_code
    new_payment.payment_method = bank_record.bank_type
    new_payment.amount_paid = bank_record.amount
    new_payment.status = bank_record.status
    new_payment.save()

    # if payment is successful
    if bank_record.is_success:

        # to get the total price of items in cart
        cart_items = Cart.objects.filter(user=request.user)
        total_price = 0
        if cart_items:
            for item in cart_items:
                total_price += item.course.price

        # to create order object
        new_order = Order()
        new_order.user = current_user
        new_order.payment = new_payment
        new_order.total_price = total_price
        new_order.tracking_code = bank_record.tracking_code
        new_order.save()

        # to create order items from cart's item
        new_order_item = Cart.objects.filter(user=current_user)
        for item in new_order_item:
            OrderItem.objects.create(
                order=new_order,
                course=item.course,
                quantity=1
            )

        # To clear user's Cart
        Cart.objects.filter(user=current_user).delete()

        messages.success(request, "Your order has been places successfully")

        # if payment was success
        send_mail(
            subject='test',
            message='test',
            from_email=mysettings.EMAIL_HOST_USER,
            recipient_list=['khademmilad@gmail.com'], # user's Email (request.user.email)
            fail_silently=False
        )
        return render(request, 'order/success_payment.html', context)

    # if payment was failure
    else:
        # To clear user's Cart
        Cart.objects.filter(user=current_user).delete()

    return render(request, 'order/failure_payment.html', context)