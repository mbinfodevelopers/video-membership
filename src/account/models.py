from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

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


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=100, blank=False, null=False)
    about_teacher = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, null=True)
    linkedin_account = models.URLField(max_length=250, blank=True, null=True)
    instagram_account = models.URLField(max_length=250, blank=True, null=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    twitter_account = models.URLField(max_length=250, blank=True, null=True)
    stackoverflow_account = models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.teacher.username


class Student(models.Model):
    student = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username


# Creating a student model after the account model is created
@receiver(post_save, sender=Account)
def create_student_object(sender, instance, created, *args, **kwargs):
    if not instance.is_admin:
        student, created = Student.objects.get_or_create(student=instance)
        student.save()
