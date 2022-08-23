from django.db import models

from account.models import Account


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='یوز پرداخت کننده ')
    payment_number = models.CharField(max_length=100, verbose_name='آیدی پرداخت ')
    payment_method = models.CharField(max_length=100, verbose_name='روش پرداخت ')
    amount_paid = models.CharField(max_length=100, verbose_name='مبلغ پرداخت شده ')
    status = models.CharField(max_length=100, verbose_name='وضعیت پرداخت ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد ')


    def __str__(self):
        return self.payment_number

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural ='لیست پرداخت ها '