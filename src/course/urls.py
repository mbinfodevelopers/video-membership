from django.urls import path
from . import views



urlpatterns = [

    path('', views.all_courses, name="all_courses"),
    path('<slug:category_slug>/', views.all_courses, name="course_by_category"),
    path('<slug:category_slug>/<slug:course_slug>/', views.course_detail, name="course_detail"),
]