from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout", views.logout_view, name='logout'),
    path('profile/dashboard/<user_id>/', views.profile_view, name='profile'),
    path('profile/editprofile/<user_id>/', views.edit_account_view, name='edit_account_view'),
    path('profile/free_course/', views.get_courses, name='get_courses'),

]