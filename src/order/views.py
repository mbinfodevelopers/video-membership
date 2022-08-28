from django.shortcuts import render
from course.models import Course
from order.models import Order, OrderItem
from django.http import JsonResponse
import json

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

    # fix later
    print('cartItems', cartItems)



    context['cartItems'] = cartItems
    return render(request, 'store/order.html', context)


def cart(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user

        # return all objects from OrderItem's model
        order, created = Order.objects.get_or_create(user=current_user, is_paid=False)
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


def update_item(request):
    # get the data from ajax response
    data = json.loads(request.body)

    courseId = data['courseId']
    action = data['action']

    print('courseid', courseId)
    print('action', action)

    current_user = request.user
    course = Course.objects.get(id=courseId)
    order, created = Order.objects.get_or_create(user=current_user, is_paid=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, course=course)

    if action == 'add':
        pass
        # orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)