from django.shortcuts import render, redirect
from order.models import Order, Cart


def order(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        order, created = Order.objects.get_or_create(user=current_user, is_paid=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        # if user is not authenticated (fix later)
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    # fix later number of cart items
    print('cartItems', cartItems)

    context['cartItems'] = cartItems
    return render(request, 'store/order.html', context)


def checkout(request):
    context = {}
    cart_item = Cart.objects.filter(user=request.user)
    context['cart_item'] = cart_item

    return render(request, 'store/checkout.html', context)