from django.shortcuts import get_object_or_404, render
from django.views import View

from hexlet_django_blog.article import models


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = models.Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={'articles': articles},
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(models.Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={'article': article},
        )
