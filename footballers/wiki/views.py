from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
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


def about(request):
    return render(request, 'wiki/about.html', {'menu': menu, 'title': 'Footballers-wiki about page'})


def add_article(request):
    return HttpResponse("Add article")


def contact(request):
    return HttpResponse("Contact")


def login(request):
    return HttpResponse("login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>pageNotFound</h1>')


def show_article(request, article_id):
    return HttpResponse(f"article id = {article_id}")


