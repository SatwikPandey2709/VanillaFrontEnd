from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.homepage, name="homepage"),
    path('welcome/', views.welcome, name="welcome-page"),
    path('login/', views.login, name="login-page"),
    path('signup/', views.signup, name="signup-page"),
    path('reset-password/', views.reset, name="reset-password"),
    path('explore/', views.explore, name="explore"),
    path('profile/', views.profile, name="profile"),
    path('messages/', views.messages, name="messages"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('posts/', views.posts, name="posts"),
    path('followers/', views.followers, name="followers"),
    path('following/', views.following, name="following"),
    path('bookmarks/', views.bookmarks, name="bookmarks"),
    path('purchased/', views.purchased, name="purchased"),
    path('settings/', views.settings, name="settings"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)