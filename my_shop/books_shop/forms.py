from django.forms import ModelForm

from books_shop.models import Book


class BookForm(ModelForm):
    '''Форма книги и ее поля, которые мы будем показывать пользователю
        Передается эта форма в ctx в views.py и рендерится при помощи языка шаблонизатора
    '''
    class Meta:
        model = Book
        fields = {field.name for field in Book._meta.fields}
