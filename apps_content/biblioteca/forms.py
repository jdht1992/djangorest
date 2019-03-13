from django.forms import ModelForm
from django import forms

from .models import Book, Student
from django.utils.translation import gettext_lazy as _


class BookModelForm(ModelForm):
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Book
        fields = ('name', 'book_code', 'pages', 'price', 'rating', 'authors', 'publisher', 'publication_date', 'gender', 'file_book')
        labels = {
            'name': _('Name'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

