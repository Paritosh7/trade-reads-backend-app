from django.forms import ModelForm

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'description',
            'author',
            'publisher',
            'published_date',
            'pages',
            'language',
            'image',
        )