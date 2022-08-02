from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.all_courses, name="all_courses")
]