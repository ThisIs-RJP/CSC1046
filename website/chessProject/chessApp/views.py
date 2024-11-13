from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from django.contrib import messages
from django.core.cache import cache
from . import views
from .forms import *
import random

def home(request):
    return render(request, 'home.html')

def new_game(request):
    return render(request, 'create.html')
    
def join_game(request):
    return render(request, 'join.html')


class UserLoginView(LoginView):
    template_name='login.html'
    
    def form_valid(self, form):
        messages.success(self.request, f"Logged in as {self.request.user.username}")
        print(messages.get_messages(self.request))  
        return super().form_valid(form)

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
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

# DO NOT CHANGE THIS
# cache.set('game_rooms', [])
game_rooms = []

def create_game(request):
    def generate_room_code(game_rooms):
        exists = True
        while exists:
            room_code = str(random.randint(100000, 999999))
            exists = room_code in game_rooms
        return room_code

    if request.method == 'POST':
        # game_rooms = cache.get('game_rooms', [])
        room_code = generate_room_code(game_rooms)
        # cache.set('game_rooms',game_rooms.append(room_code))  # Add the generated room code to game_rooms
        game_rooms.append(room_code)
        return redirect(f'/game/{room_code}/')
    return HttpResponse(status=405)

def gameJoiner(request, room_code):
    # game_rooms = cache.get('game_rooms')
    if request.method == 'POST':
        print(game_rooms)
        if room_code in game_rooms:
            return redirect(f'/game/{room_code}/')
        else:
            return redirect(f'/notFound/')
    return HttpResponse(status=405)

# Can change now

def notFound(request):
    return render(request, 'notFound.html')

def game(request, room_code):
    return render(request, 'game.html', {'room_code': room_code})