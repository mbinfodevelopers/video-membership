from order.models import Cart


def cart_count(request):
    context = {}
    cart_items = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    if cart_items:
        context['cart_count'] = cart_items.count()
    else:
        context['cart_count'] = 0

    return context