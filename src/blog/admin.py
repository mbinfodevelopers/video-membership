from django.contrib import admin
from django.contrib import admin
from .models import Category, Article

# admin.site.disable_action('delete_selected')


def make_published(model_admin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = 'منتشر شد.'
    else:
        message_bit = 'منتشر شدند.'
    model_admin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))


make_published.short_description = "انتشار مقالات انتخاب شده"


def make_draft(model_admin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = 'پیش نویس شد.'
    else:
        message_bit = 'پیش نویس شدند.'
    model_admin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))


make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'position']
    list_filter = ['title']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail_tag', 'author', 'get_persian_date', 'status', 'category_to_str']
    list_filter = ['title']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return " - ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = 'عضو کدام دسته بندی'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)