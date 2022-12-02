from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_article'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
        ]


# Create your views here.

class WikiHome(ListView):
    model = Footballer
    template_name = 'wiki/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Footballers-wiki main page'
        context['country_selected'] = 0
        return context

    def get_queryset(self):
        return Footballer.objects.filter(published=True)


class WikiCountry(ListView):
    model = Footballer
    template_name = 'wiki/index.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Footballer.objects.filter(country__slug=self.kwargs['country_slug'], published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Country - ' + str(context['articles'][0].country)
        context['menu'] = menu
        context['country_selected'] = context['articles'][0].country_id
        return context


class ShowArticle(DetailView):
    model = Footballer
    template_name = 'wiki/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = context['article']
        context['menu'] = menu
        return context


class AddArticle(CreateView):
    form_class = AddArticleForm
    template_name = 'wiki/add_article.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add article'
        context['menu'] = menu
        return context


# def index(request):
#     articles = Footballer.objects.all()
#     context = {
#         'articles': articles,
#         'menu': menu,
#         'title': 'Footballers-wiki main page',
#         'country_selected': 0,
#     }
#     return render(request, 'wiki/index.html', context=context)


# def show_country(request, country_id):
#     articles = Footballer.objects.filter(country_id=country_id)
#
#     if len(articles) == 0:
#         raise Http404()
#
#     context = {
#         'articles': articles,
#         'menu': menu,
#         'title': 'Footballers from country',
#         'country_selected': country_id,
#     }
#     return render(request, 'wiki/index.html', context=context)


# def show_article(request, article_slug):
#     article = get_object_or_404(Footballer, slug=article_slug)
#     context = {
#         'article': article,
#         'menu': menu,
#         'name': article.name,
#         'country_selected': article.country_id,
#     }
#     return render(request, 'wiki/article.html', context=context)


# def add_article(request):
#     if request.method == 'POST':
#         form = AddArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddArticleForm()
#     return render(request, 'wiki/add_article.html', {'form': form, 'menu': menu, 'title': 'Add article'})


def about(request):
    return render(request, 'wiki/about.html', {'menu': menu, 'title': 'Footballers-wiki about page'})


def contact(request):
    return HttpResponse("Contact")


def login(request):
    return HttpResponse("login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>pageNotFound</h1>')
