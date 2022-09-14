from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('', views.all_blog, name="all_blog"),
    path('category/<slug:slug>', views.category, name="category"),
    path('article/<slug:slug>', views.article_detail, name="article_detail")
]