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
    post = get_object_or_404(Article, id=id)
    context = {'post': post}
    return render(request, 'detail.html', context)