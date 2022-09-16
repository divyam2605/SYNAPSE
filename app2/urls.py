from django.urls import path
from . import views

urlpatterns = [
    path('', views.countries_api, name="index")
]
