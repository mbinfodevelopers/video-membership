from django.contrib import admin

from .models import Course,Category,Video,Comment

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Comment)
