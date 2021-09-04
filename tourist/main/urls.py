from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('planmytrip/', views.planmytrip, name='planmytrip'),
    path('explore/', views.explore, name="explore")
]
