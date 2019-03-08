from django.forms import ModelForm

from .models import Book


class BookModelForm(ModelForm):
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Book
        fields = ('name', 'book_code', 'pages', 'price', 'rating', 'authors', 'publisher', 'publication_date', 'gender', 'file_book')
