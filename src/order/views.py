from django.shortcuts import render, redirect
from course.models import Course
from order.models import Order, OrderItem, Cart
from django.http import JsonResponse
import json
from django.contrib import messages


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

def viewcart(request):
    context = {}
    cart = Cart.objects.filter(user=request.user)
    context['cart'] = cart
    return render(request, 'store/cart.html', context)

def delete_cart_item(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            course_id = int(request.POST.get('course_id'))
            if Cart.objects.filter(user=request.user, course_id=course_id):
                cartitem = Cart.objects.get(course_id=course_id, user=request.user)
                cartitem.delete()

                return JsonResponse({'status': "Deleted Successfully"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')


# def cart(request):
#     context = {}
#     if request.user.is_authenticated:
#         current_user = request.user
#
#         # return all objects from OrderItem's model
#         order, created = Order.objects.get_or_create(user=current_user, is_paid=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#
#         # if user is not authenticated (fix later)
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#
#     context['items'] = items
#     context['order'] = order
#     return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        order, created = Order.objects.get_or_create(user=current_user, is_paid=False)
        items = order.orderitem_set.all()
    else:
        items = []

        # if user is not authenticated (fix later)
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context['items'] = items
    context['order'] = order
    return render(request, 'store/checkout.html', context)


# def update_item(request):
#     # get the data from ajax response
#     data = json.loads(request.body)
#
#     courseId = data['courseId']
#     action = data['action']
#
#     current_user = request.user
#     course = Course.objects.get(id=courseId)
#     order, created = Order.objects.get_or_create(user=current_user, is_paid=False)
#
#     orderItem, created = OrderItem.objects.get_or_create(order=order, course=course)
#
#     if action == 'add':
#         orderItem.quantity = 1
#     elif action == 'remove':
#         orderItem.quantity = 0
#
#     orderItem.save()
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#
#     return JsonResponse('Item was added', safe=False)


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            course_id = int(request.POST.get('course_id'))
            course_check = Course.objects.get(id=course_id)
            if course_check:
                if Cart.objects.filter(user=request.user.id, course_id=course_id):
                    return JsonResponse({'status': 'Course Already in Cart'})
                else:
                    course_qyt = 1
                    Cart.objects.create(user=request.user, course_id=course_id, course_qyt=course_qyt)
                    return JsonResponse({'status': 'Course addes successfuly'})
            else:
                return JsonResponse({'status': 'No such course found'})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')

