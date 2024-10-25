from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.UserSignupView.as_view(), name="register"),
]
