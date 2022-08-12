from django.contrib import admin
from .models import Category



class AdminCategory(admin.ModelAdmin):
    prepopulated_fields =  {'slug':('category_name',)}
    list_display = ['category_name','slug','description']


admin.site.register(Category,AdminCategory)