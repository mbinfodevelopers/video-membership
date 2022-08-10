from django.contrib import admin
from .models import Category



class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name','slug','description']


admin.site.register(Category,AdminCategory)