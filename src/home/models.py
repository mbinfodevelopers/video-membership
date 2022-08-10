from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name= models.CharField(max_length=55,unique=True,verbose_name='دسته بندی کلی ')
    slug= models.SlugField(max_length=150,unique=True, verbose_name=' آدرس اسلاگ ')
    description= models.TextField(max_length=255,blank=True, verbose_name='توضیحات ')


    class Meta:
        verbose_name= 'دسته بندی'
        verbose_name_plural ='دسته بندی کلی'


    def __str__(self):
        return self.category_name

    #FOR GET SLUG URL CATEGORIES
    #__________________________
    def get_url(self):
        return reverse('course_by_category',args=[self.slug])