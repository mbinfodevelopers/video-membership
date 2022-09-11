import logging
from django.http import Http404, HttpResponse
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from payment.models import Payment
from django.db.models import Q
from order.models import Order, OrderItem, Cart
from django.contrib import messages


def go_to_gateway_view(request):

    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 50000

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
    current_user = request.user
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)

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

        # to create order object
        new_order = Order()
        new_order.user = current_user
        new_order.payment = new_payment
        # new_order.total_price = ???
        # new_order.ip = ???
        new_order.tracking_code = bank_record.tracking_code
        new_order.save()


        # to create order items form cart items
        new_order_item = Cart.objects.filter(user=current_user)
        for item in new_order_item:
            OrderItem.objects.create(
                order=new_order,
                course=item.course,
                quantity=1
            )

        # To clear user's Cart
        Cart.objects.filter(user=current_user).delete()

        messages.success(request, "Your order has benn places successfully")

        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")