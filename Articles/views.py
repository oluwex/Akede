from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.


def index(request):
    posts = Article.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def detail(request, id=None, slug=None):
    # article = get_object_or_404(Article, pk=id)
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article
    }
    return render(request, 'article/details.html', context)