from django.db.models import Count

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_article'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        countries = Country.objects.annotate(Count('footballer'))
        # countries = Country.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)  # pop add_article

        context['menu'] = user_menu

        context['countries'] = countries
        if 'country_selected' not in context:
            context['country_selected'] = 0
        return context
