from django.urls import path
from . import views
from azbankgateways.urls import az_bank_gateways_urls
from .bank import go_to_gateway_view, callback_gateway_view

app_name = 'order'

urlpatterns = [
    path('', views.order, name='order'),
    # path('cart/', views.cart, name='cart'),
    path('cart/', views.viewcart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    # path('update_item/', views.update_item, name='update_item'),
    path('add-to-cart/', views.addtocart, name='add-to-card'),
    path('delete-cart-item', views.delete_cart_item, name='delete-cart-item'),
    path('place-order', views.placeorder, name="placeorder"),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gatewey/', go_to_gateway_view, name='go-to-gatewey'),
    path('callback-gateway/', callback_gateway_view),
]