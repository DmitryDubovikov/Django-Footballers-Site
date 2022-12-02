from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].empty_label = "not selected"

    class Meta:
        model = Footballer
        fields = ['name', 'slug', 'content', 'photo', 'published', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Length is more than 200')
        return name
