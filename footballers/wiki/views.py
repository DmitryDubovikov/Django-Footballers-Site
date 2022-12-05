from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
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
        return Footballer.objects.filter(published=True).select_related('country')


class WikiCountry(DataMixin, ListView):
    model = Footballer
    template_name = 'wiki/index.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Footballer.objects.filter(country__slug=self.kwargs['country_slug'], published=True).select_related(
            'country')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        country = Country.objects.get(slug=self.kwargs['country_slug'])
        mixin_context = self.get_user_context(title='Country - ' + str(country.name), country_selected=country.pk)
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'wiki/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(mixin_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def about(request):
    return render(request, 'wiki/about.html', {'menu': menu, 'title': 'Footballers-wiki about page'})


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'wiki/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title="Contact us")
        return dict(list(context.items()) + list(mixin_context.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'wiki/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title="Authentication ")
        return dict(list(context.items()) + list(mixin_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
