from django.urls import path
from .views import (
    login_view,
    # home_view,
    register_view,
    logout_view,
    edit_account_view,
    profile_view
)


app_name = 'account'

urlpatterns = [
    # path("", home_view, name="home"),
    path('login/', login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout", logout_view, name='logout'),
    path('<user_id>/edit/', edit_account_view, name="edit"),
    path('profile/<user_id>/', profile_view, name='profile')

]