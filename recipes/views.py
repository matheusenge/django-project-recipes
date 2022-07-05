from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE

from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')
