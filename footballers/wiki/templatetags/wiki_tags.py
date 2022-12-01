from django import template
from wiki.models import *

register = template.Library()


@register.simple_tag(name='get_countries')
def get_countries(filter=None):
    if not filter:
        return Country.objects.all()
    else:
        return Country.objects.filter(pk=filter)


@register.inclusion_tag('wiki/list_countries.html')
def show_countries(sort=None, country_selected=0):
    if not sort:
        countries = Country.objects.all()
    else:
        countries = Country.objects.order_by(sort)

    return {"countries": countries, "country_selected": country_selected}
