from django.db import models

# Create your models here.
from account.models import Account



class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    STATUS = (
        ('new course', 'new course'),
        ('Course in progress', 'Course in progress'),
        ('Course update', 'Course update'),
        ('The course is over', 'The course is over'),
    )

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # teacher
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(),
    image = models.ImageField(upload_to='media/Course/', blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(blank=True, null=True)
    sell_count = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'course',
    #     verbose_name_plural ='course_section'


class Comment(models.Model):
    STATUS = (
        ('readed', 'readed'),
        ('Unreaded', 'Unreaded'),
        ('close', 'close'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=350, null=True, blank=True)
    author_user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    user_ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=25, choices=STATUS, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    video = models.FileField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title