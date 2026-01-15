from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'article_index.html',
            context={'application_name': 'Статьи'},
        )
