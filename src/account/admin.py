from django.contrib import admin
from .models import Account, Teacher, Student

admin.site.register(Account)
admin.site.register(Student)
admin.site.register(Teacher)