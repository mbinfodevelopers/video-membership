from django.shortcuts import render
from order.models import Order, OrderItem

def order(request):
    context = {}
    return render(request, 'store/order.html', context)


def cart(request):
    context = {}
    if request.user.is_authenticated:
        account = request.user
        order, created = Order.objects.get_or_create(user=account, is_paid=False)
        print(order.__dict__, created)
        items = order.orderitem_set.all()
    else:
        items = []
    context['items'] = items
    print(items[0].__dict__)
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)