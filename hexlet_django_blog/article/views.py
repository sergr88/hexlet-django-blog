from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'article_index.html',
            context={'application_name': 'Статьи'},
        )


def show(request, tags, article_id):
    return render(
        request,
        'article_show.html',
        context={'tags': tags, 'article_id': article_id},
    )
