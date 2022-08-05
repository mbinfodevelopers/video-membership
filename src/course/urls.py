from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.index_homepage, name="home_view")
]