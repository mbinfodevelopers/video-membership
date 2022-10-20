from order.models import Order, OrderItem, Cart
from django.shortcuts import render, redirect
from django.http import JsonResponse
from course.models import Course
from django.contrib import messages


def view_cart(request):
    context = {}
    cart = Cart.objects.filter(user=request.user)
    messages.success(request, 'cart')
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


def add_to_cart(request):
    messages.success(request, 'haminjam')
    if request.method == 'POST':
        if request.user.is_authenticated:
            course_id = int(request.POST.get('course_id'))
            course_check = Course.objects.get(id=course_id)
            if course_check:
                if Cart.objects.filter(user=request.user.id, course_id=course_id):
                    # messages.warning(request, "Course Already in Cart")
                    return JsonResponse({'status': 'Course Already in Cart'})
                else:
                    course_qyt = 1
                    Cart.objects.create(user=request.user, course_id=course_id, course_qyt=course_qyt)
                    # messages.success(request, "Course added successfuly")
                    return JsonResponse({'status': 'Course added successfuly'})
            else:
                return JsonResponse({'status': 'No such course found'})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')