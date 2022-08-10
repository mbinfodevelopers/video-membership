from django.contrib import admin

from .models import Course,Video,Comment


class AdminCourse(admin.ModelAdmin):
    list_display = ['title','category','is_active','status','teacher']

class AdminVideo(admin.ModelAdmin):
    list_display = ['title','course','create_date']

class AdminComment(admin.ModelAdmin):
    list_display = ['course','comment','status','user_ip','is_active']


admin.site.register(Course,AdminCourse)
admin.site.register(Video,AdminVideo)
admin.site.register(Comment,AdminComment)
