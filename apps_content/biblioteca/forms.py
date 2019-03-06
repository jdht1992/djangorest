from django.forms import ModelForm

from .models import Book


class BookModelForm(ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'book_code', 'pages', 'price', 'rating', 'authors', 'publisher', 'publication_date', 'gender')
