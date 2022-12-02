from django.contrib import admin

# Register your models here.
from .models import *


class FootballerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'photo', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Footballer, FootballerAdmin)
admin.site.register(Country, CountryAdmin)
