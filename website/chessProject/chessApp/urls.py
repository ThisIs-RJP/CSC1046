from django.contrib import admin
from django.urls import path, include
from . import views
from .forms import *

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('', views.home, name='home'),
    path('new_game/', views.new_game, name='new_game'),
    path('join_game/', views.join_game, name='join_game'),
    path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', views.logout_user, name='logout'),]
