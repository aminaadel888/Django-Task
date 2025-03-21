"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from django.contrib.auth.views import *
from trainee.views import *




def home(request):
    return render(request,'base.html')

urlpatterns = [
    path('', TraineeLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', RegisterView, name='register'),
    path('logout/', TraineeLogoutView.as_view(next_page='login'), name='logout'),
    path('',home,name='home'),
    path('trainees/', include('trainee.urls')),
    path('courses/',include('course.urls')),

]
