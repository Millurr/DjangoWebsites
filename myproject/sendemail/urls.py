from django.contrib import admin
#from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.emailView, name='email'),
    path('success/', views.successView, name='success')
]