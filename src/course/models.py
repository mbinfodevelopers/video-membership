from django.db import models
from django.urls import reverse
from jalali_date import datetime2jalali, date2jalali
from account.models import Account
from home.models import Category


def get_course_image_filepath(self, filename):
    return 'course/course_images/' + str(self.pk) + '/course_image.png'


def get_default_course_image():
    return "course/course_default_images/default_course_image.png"


class Course(models.Model):
    STATUS = (
        ('New Course', 'New Course'),
        ('Course in progress', 'Course in progress'),
        ('Course update', 'Course update'),
        ('The course is over', 'The course is over'),
    )

    title = models.CharField(max_length=150, unique=True,verbose_name=' عنوان ')
    slug = models.SlugField(max_length=200, unique=True,verbose_name=' آدرس اسلاگ ')
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name=' مدرس دوره ')
    description = models.TextField(blank=True, null=True,verbose_name=' توضیحات ')
    course_content = models.TextField(blank=True, null=True, verbose_name='توضیحات کوتاه')
    price = models.IntegerField(blank=True,null=True,verbose_name='قیمت ')
    image = models.ImageField(upload_to=get_course_image_filepath, blank=True, null=True, default=get_default_course_image,verbose_name='تصویر دوره ')
    status = models.CharField(max_length=25, choices=STATUS, blank=True,verbose_name=' وضعیت ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=' دسته بندی ')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name=' تاریخ ایجاد ')
    modify_date = models.DateTimeField(auto_now=True,verbose_name=' تاریخ آپدیت ')
    view_count = models.IntegerField(blank=True, null=True,verbose_name=' تعداد بازدید')
    sell_count = models.IntegerField(blank=True, null=True,verbose_name=' تعداد فروش ')
    is_active = models.BooleanField(default=True,verbose_name='وضعیت فعال بودن دوره')
    is_free = models.BooleanField(default=True,verbose_name='رایگان ')

    def __str__(self):
        return self.title


        # This Function For Get Category And Course Url
        # ----------------------------------------------
    def get_url(self):
        return reverse('course_detail', args=[self.category.slug, self.slug])


        # This Function For Get Persian date
        # ----------------------------------
    def get_persian_date(self):
        return date2jalali(self.create_date)


    class Meta:
        verbose_name = 'دوره',
        verbose_name_plural =' دوره ها'


    @property
    def count_video(self):
        return self.video_set.all().count()


def get_video_filepath(self, filename):
    course_id = self.course.pk
    return f'videos/{course_id}/{course_id}.mp4'


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True,verbose_name='دوره مرتبط')
    title = models.CharField(max_length=150, unique=True,verbose_name=' عنوان ')
    description = models.TextField(blank=True, null=True,verbose_name=' توضیحات ')
    slug = models.SlugField(max_length=200, unique=True,verbose_name=' آدرس اسلاگ ')
    video = models.FileField(null=True, blank=True, upload_to=get_video_filepath,verbose_name=' ویدیو دوره ')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name=' تاریخ ایجاد ')
    modify_date = models.DateTimeField(auto_now=True,verbose_name=' تاریخ آپدیت ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویدیو',
        verbose_name_plural ='بخش ویدیو ها'


class Comment(models.Model):
    STATUS = (
        ('readed', 'readed'),
        ('unreaded', 'unreaded'),
        ('close', 'close'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True,verbose_name=' دوره مرتبط ')
    comment = models.CharField(max_length=350, null=True, blank=True,verbose_name=' نظرهات ')
    author_user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True,verbose_name=' کاربر مربوط ')
    user_ip = models.CharField(max_length=20, blank=True,verbose_name=' آی پی کاربر ')
    status = models.CharField(max_length=25, choices=STATUS, blank=True,verbose_name=' وضعیت پیام ')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name=' تاریخ ایجاد ')
    modify_date = models.DateTimeField(auto_now=True,verbose_name=' تاریخ آپدیت ')
    is_active = models.BooleanField(default=True,verbose_name=' وضعیت فعال بودن ')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'نظر',
        verbose_name_plural ='بخش نظرات'