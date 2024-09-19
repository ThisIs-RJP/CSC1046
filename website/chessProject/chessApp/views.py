from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def new_game(request):
    return render(request, 'home.html')
    
def join_game(request):
    return render(request, 'home.html')
    
def login(request):
    return render(request, 'home.html')