from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import APIForm
import requests


def index(request):
    response = requests.get("https://dog.ceo/api/breeds/list/all").json()
    return render(request, 'index.html', response)


def index2(request):
    for_breed = request.GET.get('for_breed', '')
    for_sub_breed = request.GET.get('for_sub_breed', '')
    url_first = "https://dog.ceo/api/breed/"
    url_last = "/images/random"
    url = url_first + for_breed + '/' + for_sub_breed + url_last
    response = requests.get(url).json()
    return render(request, 'photo.html', response)


