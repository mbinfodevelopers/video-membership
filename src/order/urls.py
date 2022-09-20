from django.urls import path
from . import views
from order import cart

app_name = 'order'

urlpatterns = [
    path('', views.order, name='order'),
    path('cart/', cart.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/', cart.add_to_cart, name='add-to-card'),
    path('delete-cart-item', cart.delete_cart_item, name='delete-cart-item'),
]
