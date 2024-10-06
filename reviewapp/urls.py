"""
URL configuration for aiaas project.

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
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home2, name='home2'),
    path('', views.home3, name='home3'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contacts/', views.contacts, name='contacts'),
    path('404/', views.not_found, name='404'),
    path('faq/', views.faq, name='faq'),
    path('help/', views.help, name='help'),
    path('companies-landing/', views.companies, name='companies'),
    path('all-categories/', views.categories, name='all-categories'),
    path('category-companies-listings-filterstop/', views.filterstop, name='category-companies-listings-filterstop'),
    path('write-review/', views.write_review, name='write-review'),


    
]

