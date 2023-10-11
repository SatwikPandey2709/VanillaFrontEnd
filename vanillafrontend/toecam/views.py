from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def reset(request):
    return render(request, 'resetpass.html')

def homepage(request):
    return render(request, 'homepage.html')

def welcome(request):
    return render(request, 'intro.html')

def explore(request):
    return render(request, 'explore.html')

def profile(request):
    return render(request, 'profile.html')

def messages(request):
    return render(request, 'messages.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def posts(request):
    return render(request, 'posts.html')

def followers(request):
    return render(request, 'followers.html')

def following(request):
    return render(request, 'following.html')