from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/'),
    # path('intro/'),
    path('login/', views.login, name="login-page"),
    path('signup/', views.signup, name="signup-page"),
    # path('reset-password/'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)