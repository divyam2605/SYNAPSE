from django.shortcuts import render
import requests


def countries_api(request):
    response = requests.get("https://api.covid19api.com/countries").json()
    return render(request, "index2.html", {"response": response})
