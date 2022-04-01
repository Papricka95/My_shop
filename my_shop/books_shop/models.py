from django.db import models


# Create your models here.
class Book(models.Model):
    CHOICE_PUBLISHER = (
        ('ast', 'АСТ'),
        ('eksmo', 'Эксмо'),
    )

    name_author = models.CharField(max_length=50, verbose_name='Имя автора')
    surname_author = models.CharField(max_length=50, verbose_name='Фамилия автора')
    name_book = models.CharField(max_length=255, verbose_name='Название книги')
    genre_of_book = models.CharField(max_length=50, verbose_name="Жанр книги", default="Без жанра")
    date_of_publication = models.DateField(auto_now_add=False, auto_now=False, verbose_name='Дата публикации')
    publisher = models.CharField(max_length=20, choices=CHOICE_PUBLISHER, verbose_name='Издатель')
    salary = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='Цена')

    def __str__(self):
        return 'Имя Автора - {0}, Фамилия автора - {1}, Название книги - {2}, Жанр книги - {3}, Дата публикации - {4}, ' \
               'Издатель - {5}, Цена - {6}'.format(self.name_author, self.surname_author, self.name_book,
                                                   self.genre_of_book, self.date_of_publication, self.publisher,
                                                   self.salary)

    def dict(self):
        '''
        этот метод предназначен для того, чтоб был валидным аргумент функции JsonResponse(data, ..), где data
        должен быть dict
        '''
        obj = {
            'name': self.name_book,  # ссылка на поле класса Human
            'surname': self.name_author,
            'birth': self.surname_author,
            'company': self.date_of_publication,
            'position': self.publisher,
            # 'language': self.language,
            'salary': self.salary
        }
        return obj
