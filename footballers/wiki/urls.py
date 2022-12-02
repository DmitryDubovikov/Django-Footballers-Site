from django.urls import path
from .views import *

urlpatterns = [
    path('', WikiHome.as_view(), name='home'),
    path('about', about, name='about'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('country/<slug:country_slug>/', WikiCountry.as_view(), name='country'),
]
