from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.


def index(request):
    posts = Article.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def detail(request, id=None):
    article = get_object_or_404(Article, pk=id)
    context = {'article': article}
    return render(request, 'article/details.html', context)