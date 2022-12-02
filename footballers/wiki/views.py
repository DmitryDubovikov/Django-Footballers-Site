from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_article'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
        ]


# Create your views here.

def index(request):
    articles = Footballer.objects.all()
    context = {
        'articles': articles,
        'menu': menu,
        'title': 'Footballers-wiki main page',
        'country_selected': 0,
    }
    return render(request, 'wiki/index.html', context=context)


def show_country(request, country_id):
    articles = Footballer.objects.filter(country_id=country_id)

    if len(articles) == 0:
        raise Http404()

    context = {
        'articles': articles,
        'menu': menu,
        'title': 'Footballers from country',
        'country_selected': country_id,
    }
    return render(request, 'wiki/index.html', context=context)


def show_article(request, article_slug):
    article = get_object_or_404(Footballer, slug=article_slug)
    context = {
        'article': article,
        'menu': menu,
        'name': article.name,
        'country_selected': article.country_id,
    }
    return render(request, 'wiki/article.html', context=context)


def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddArticleForm()
    return render(request, 'wiki/add_article.html', {'form': form, 'menu': menu, 'title': 'Add article'})


def about(request):
    return render(request, 'wiki/about.html', {'menu': menu, 'title': 'Footballers-wiki about page'})


def contact(request):
    return HttpResponse("Contact")


def login(request):
    return HttpResponse("login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>pageNotFound</h1>')
