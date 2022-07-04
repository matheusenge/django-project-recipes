from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def contact(request):
    pass


def about(request):
    pass
