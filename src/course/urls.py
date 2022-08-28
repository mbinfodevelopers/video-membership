from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [

    path('', views.all_courses, name="courses"),
    path('<slug:category_slug>/', views.all_courses, name="course_by_category"),
    path('<slug:category_slug>/<slug:course_slug>/', views.course_detail, name="course_detail"),
]