from django.contrib import admin
from django.urls import path
from agroplus import views
urlpatterns = [
    path('', views.home, name='home'),
    path('farmercorner', views.farmercorner, name='farmercorner'),
    path('Buy', views.Buy, name='Buy'),
    path('Sell', views.Sell, name='Sell'),
]