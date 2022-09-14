from django.contrib import admin
from .models import Account, Teacher, Student, Skill


class AdminAccount(admin.ModelAdmin):
    list_display = ['email', 'userAccount_image', 'username', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'when_user_joined',]
    readonly_fields = ['email', 'password']
    list_filter = ['email', 'username']


class AdminTeacher(admin.ModelAdmin):
    list_display = ['teacher', 'teacher_name']
    list_filter = ['teacher', 'teacher_name']


class AdminStudent(admin.ModelAdmin):
    list_display = ['student']


class AdminSkill(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Account, AdminAccount)
admin.site.register(Teacher, AdminTeacher)
admin.site.register(Student, AdminStudent)
admin.site.register(Skill, AdminSkill)