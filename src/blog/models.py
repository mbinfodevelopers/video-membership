from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['-position']

    def __str__(self):
        return self.title


def get_Article_image_filepath(self, filename):
    return 'article/article_images/' + str(self.pk) + '/article.png'


def get_default_article_image():
    return "article/article_images/article.png"


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منشتر شده'),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category, related_name='the_articles', verbose_name='دسته بندی ')
    description = models.TextField(verbose_name='محتوای مقاله')
    thumbnail = models.ImageField(upload_to=get_Article_image_filepath, blank=True, null=True, default=get_default_article_image, verbose_name='تصویر مقاله ')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت مقاله')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_persian_date(self):
        return jalali_converter(self.publish)
    get_persian_date.short_description = 'زمان انتشار'

    def category_published(self):
        return self.category.filter(status=True)

