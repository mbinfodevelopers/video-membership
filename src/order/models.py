from django.db import models
from account.models import Account
from course.models import Course
from payment.models import Payment


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, verbose_name='کاربر سفارش دهنده')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع پرداخت')
    total_price = models.FloatField(blank=True, null=True, verbose_name='جمع سفارش')
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    update_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')
    tracking_code = models.CharField(max_length=200, null=True, blank=True, verbose_name='شماره پیگیری')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش مربوط')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='دوره مورد نظر')
    order_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش محصول')
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = 'سفارش محصول'
        verbose_name_plural = 'محصولات سفارش داده شده'


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_qyt = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'آیتم های سبد خرید'