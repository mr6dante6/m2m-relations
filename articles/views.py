from django.shortcuts import render
from .models import Article


def articles_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    template = 'articles/news.html'
    return render(request, template, context)
