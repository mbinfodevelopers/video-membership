from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

# class OrderProduct_line(admin.TabularInline):
#     model = OrderItem
#     readonly_fields = ('user', 'course', 'product_price')
#     can_delete = False
#     extra = 0
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['user', 'order_number', 'status', 'is_paid']
#     list_filter = ['user']
#     readonly_fields = ('user', 'order_number', 'order_total', 'status', 'ip', 'is_paid')
#     inlines = [OrderProduct_line]
#
#
# class OrderProductAdmin(admin.ModelAdmin):
#     list_display = ['user', 'course', 'product_price', 'order_at']
#     list_filter = ['user']
#
#
# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderProductAdmin)

