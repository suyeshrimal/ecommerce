from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
path('login',login),
path('register',user_register),
    # path('auth/', include('djoser.urls')),
    # path('auth/',include('djoser.urls.authtoken')),
]