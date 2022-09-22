from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout", views.logout_view, name='logout'),
    path('<user_id>/edit/', views.edit_account_view, name="edit"),
    path('profile/<user_id>/', views.profile_view, name='profile'),

]