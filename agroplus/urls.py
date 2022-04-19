from django.contrib import admin
from django.urls import path
from agroplus import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home1', views.home1, name='home1'),
]