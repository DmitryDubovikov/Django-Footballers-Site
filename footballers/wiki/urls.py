from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('add_article/', add_article, name='add_article'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('article/<slug:article_slug>/', show_article, name='article'),
    path('country/<int:country_id>/', show_country, name='country'),
]
