from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from . import views
from .forms import *

def home(request):
    return render(request, 'home.html')

def new_game(request):
    return render(request, 'home.html')
    
def join_game(request):
    return render(request, 'home.html')
    
def login(request):
    return render(request, 'home.html')


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home.html")


class UserLoginView(LoginView):
    template_name='home.html'


def logout_user(request):
    logout(request)
    return redirect("/")

