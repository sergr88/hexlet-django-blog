from django.shortcuts import render
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


def show(request, tags, article_id):
    return render(
        request,
        'article_show.html',
        context={'tags': tags, 'article_id': article_id},
    )
