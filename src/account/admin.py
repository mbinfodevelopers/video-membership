from django.contrib import admin
from .models import Account, Teacher, Student, Skill

admin.site.register(Account)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Skill)