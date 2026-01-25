from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def about(request):
    return render(request, 'about.html')
