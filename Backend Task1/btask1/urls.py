
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('photo/', views.index2, name="index2"),
]
