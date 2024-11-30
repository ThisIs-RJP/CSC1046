from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from django.contrib import messages
from . import views
from .forms import *

def home(request):
    return render(request, 'home.html')

def new_game(request):
    return render(request, 'home.html')
    
def join_game(request):
    return render(request, 'home.html')

def game(request):
    return render(request, 'game.html')

class UserLoginView(LoginView):
    template_name='login.html'
    
    def form_valid(self, form):
        messages.success(self.request, f"Logged in as {self.request.user.username}")
        print(messages.get_messages(self.request))  

        return super().form_valid(form)

class UserSignupView(CreateView):
    model         = User
    form_class    = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f"Successfully registered as {user.username}")
        print(messages.get_messages(self.request))  

        return redirect("home")


def logout_user(request):
    logout(request)

    return redirect("/")
