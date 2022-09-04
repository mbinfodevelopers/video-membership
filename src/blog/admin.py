from django.contrib import admin
from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'position']
    list_filter = ['title']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail', 'get_persian_date', 'status', 'category_to_str']
    list_filter = ['title']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']

    def category_to_str(self, obj):
        return " - ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = 'عضو کدام دسته بندی'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)