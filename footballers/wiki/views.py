from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_article'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
        ]


# Create your views here.

class WikiHome(DataMixin, ListView):
    model = Footballer
    template_name = 'wiki/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title="Footballers-wiki main page")
        return dict(list(context.items()) + list(mixin_context.items()))

    def get_queryset(self):
        return Footballer.objects.filter(published=True)


class WikiCountry(DataMixin, ListView):
    model = Footballer
    template_name = 'wiki/index.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Footballer.objects.filter(country__slug=self.kwargs['country_slug'], published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Country - ' + str(context['articles'][0].country),
                                              country_selected=context['articles'][0].country_id)
        return dict(list(context.items()) + list(mixin_context.items()))


class ShowArticle(DataMixin, DetailView):
    model = Footballer
    template_name = 'wiki/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=context['article'])
        return dict(list(context.items()) + list(mixin_context.items()))


class AddArticle(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'wiki/add_article.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title="Add article")
        return dict(list(context.items()) + list(mixin_context.items()))


def about(request):
    return render(request, 'wiki/about.html', {'menu': menu, 'title': 'Footballers-wiki about page'})


def contact(request):
    return HttpResponse("Contact")


def login(request):
    return HttpResponse("login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>pageNotFound</h1>')
