from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_homepage, name="home_view")
]