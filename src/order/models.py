from django.db import models
from account.models import Account
from course.models import Course
from payment.models import Payment


class Order(models.Model):
    STATUS = (
        ('New', 'جدید'),
        ('Accepted', 'تایید شده'),
        ('Completed', 'تکمیل شده'),
        ('Cancelled', 'کنسل شده'),
    )
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, verbose_name='یوزر سفارش دهنده')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع پرداخت ')
    order_number = models.CharField(max_length=25, verbose_name='شماره سفارش')
    order_note = models.CharField(max_length=150, null=True, blank=True, verbose_name='توضیحات سفارش')
    order_total = models.FloatField(verbose_name='جمع سفارش')
    status = models.CharField(max_length=15, choices=STATUS, default='New', verbose_name='وضعیت سفارش')
    ip = models.CharField(blank=True, max_length=20, verbose_name='آی پی کاربر ')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده است  ')
    date_Order = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    update_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت ')

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'لیست سفارش ها'



class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش مربوط')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع پرداخت ')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='یوز سفارش دهنده')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='دوره مورد نظر')
    product_price = models.IntegerField(verbose_name='قیمت محصول')
    order_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش محصول')

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = 'سفارش محصول'
        verbose_name_plural = 'محصولات سفارش داده شده'