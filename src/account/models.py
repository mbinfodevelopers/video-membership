from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.html import format_html
from extensions.utils import jalali_converter


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return 'profile/profile_images/' + str(self.pk) + '/profile_image.png'


def get_default_profile_image():
    return "profile/profile_default/default_profile_image.png"


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, verbose_name='email')
    username = models.CharField(max_length=30, unique=True, verbose_name='نام و نام خانوادگی')
    time_joined = models.DateTimeField(default=timezone.now, verbose_name='زمان ثبت نام')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False, verbose_name='آیا ادمین است')
    is_active = models.BooleanField(default=True, verbose_name='حساب کاربر فعال است')
    is_staff = models.BooleanField(default=False, verbose_name='اجازه ورود به پنل ادمین')
    is_superuser = models.BooleanField(default=False, verbose_name='آیا سوپر یوزر است')
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image, verbose_name='تصویر کاربر')
    hide_email = models.BooleanField(default=True, verbose_name='مخفی بودن ایمیل کاربر')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_image/' + str(self.pk) + "/"):]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def when_user_joined(self):
       return jalali_converter(self.date_joined)
    when_user_joined.short_description = 'تاریخ ثبت نام'

    def userAccount_image(self):
        return format_html("<img width=90 height=70 style='border-radius: 5px' src='{}'>".format(self.profile_image.url))
    userAccount_image.short_description = "عکس کاربر"


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='مهارت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'


class Teacher(models.Model):
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='استاد مربوطه')
    teacher_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='نام استاد')
    about_teacher = models.TextField(blank=True, null=True, verbose_name='درباره ی استاد')
    skills = models.ManyToManyField(Skill, blank=True, verbose_name='مهارت های استاد')
    linkedin_account = models.URLField(max_length=250, blank=True, null=True, verbose_name='اکانت لینکدین')
    instagram_account = models.URLField(max_length=250, blank=True, null=True, verbose_name='اکانت اینستاگرام')
    website = models.URLField(max_length=250, blank=True, null=True, verbose_name='آدرس وب سایت')
    twitter_account = models.URLField(max_length=250, blank=True, null=True, verbose_name='اکانت توتیتر')
    stackoverflow_account = models.URLField(max_length=250, blank=True, null=True, verbose_name='اکانت استک آورفلو')

    def __str__(self):
        return self.teacher.username

    class Meta:
        verbose_name = 'استاد'
        verbose_name_plural = 'استاتید'


class Student(models.Model):
    student = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='داتشجو')

    class Meta:
        verbose_name = 'دانشجو'
        verbose_name_plural = 'دانشجویان'

    def __str__(self):
        return self.student.username


# Creating a student model after the account model is created
@receiver(post_save, sender=Account)
def create_student_object(sender, instance, created, *args, **kwargs):
    if not instance.is_admin:
        student, created = Student.objects.get_or_create(student=instance)
        student.save()
