from django.shortcuts import render, get_object_or_404, redirect, Http404, HttpResponseRedirect
from django.contrib import messages
from .models import Article
from .forms import CreateForm
# Create your views here.


def index(request):
    posts = Article.objects.all()
    context = {
        'articles': posts
    }
    return render(request, 'index.html', context)


def create_article(request):
    if not request.user.is_staff:
        raise Http404
    form = CreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.author = request.user
        new_article = form.save(commit=False)
        new_article.author = request.user
        new_article.save()
        messages.success(request, "Article successfully created.")
        return redirect("articles:home")
    context = {
        'form': form,
        'title': "Create",
    }
    return render(request, 'article/create.html', context)

def update_article(request, slug=None):
    if not request.user.is_staff:
        raise Http404
    instance = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = CreateForm(request.POST or None, request.FILES or None, instance=instance)     
        if form.is_valid():
            instance = form.save(commit=False)
            instance.updated_by = request.user
            instance.save()
            messages.success(request, "Article has been successfully updated.", extra_tags='html_safe')
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = CreateForm(instance = instance)        
    context = {
        'form': form,
        'title': "Edit",
    }
    return render(request, 'article/create.html', context)

def detail(request, slug=None):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article
    }
    return render(request, 'article/details.html', context)