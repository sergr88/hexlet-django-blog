from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    return render(request, 'index.html', context={'who': 'World'})


def about(request):
    return render(request, 'about.html')
