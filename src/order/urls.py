from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order, name='order'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/', views.add_to_cart, name='add-to-card'),
    path('delete-cart-item', views.delete_cart_item, name='delete-cart-item'),
]
