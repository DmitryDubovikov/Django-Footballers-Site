from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import *


class FootballerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'get_html_photo', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'country', 'content', 'photo', 'get_html_photo', 'published', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_html_photo')
    save_on_top = True


    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Miniature"


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Footballer, FootballerAdmin)
admin.site.register(Country, CountryAdmin)
