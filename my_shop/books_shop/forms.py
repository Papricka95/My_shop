from django.forms import ModelForm

from books_shop.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = {field.name for field in Book._meta.fields}
