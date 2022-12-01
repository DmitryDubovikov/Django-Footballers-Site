from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('addarticle/', add_article, name='add_article'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('article/<int:article_id>/', show_article, name='article'),
]
