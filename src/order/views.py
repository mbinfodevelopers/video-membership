from django.shortcuts import render
from order.models import Order, OrderItem

def order(request):
    context = {}
    return render(request, 'store/order.html', context)


def cart(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        order, created = Order.objects.get_or_create(user=current_user, is_paid=False)
        print(order.__dict__, created)
        items = order.orderitem_set.all()
    else:
        items = []

        # if user is not authenticated (fix later)
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context['items'] = items
    context['order'] = order
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        order, created = Order.objects.get_or_create(user=current_user, is_paid=False)
        print(order.__dict__, created)
        items = order.orderitem_set.all()
    else:
        items = []

        # if user is not authenticated (fix later)
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context['items'] = items
    context['order'] = order
    return render(request, 'store/checkout.html', context)