from django.db import models
from account.models import Account


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

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

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(),
    image = models.ImageField(upload_to=get_course_image_filepath, blank=True, null=True, default=get_default_course_image)
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


class Comment(models.Model):
    STATUS = (
        ('readed', 'readed'),
        ('unreaded', 'unreaded'),
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