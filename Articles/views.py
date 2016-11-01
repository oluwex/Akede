from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    posts = Article.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)