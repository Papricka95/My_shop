from django.db import models


# Create your models here.
class Book(models.Model):
    CHOICE_PUBLISHER = (
        ('ast', 'АСТ'),
        ('eksmo', 'Эксмо'),
    )
    #
    # POSITION_CHOICES = (
    #     ('senior', 'Senior'),
    #     ('middle', 'Middle'),
    #     ('junior', 'Junior')
    # )

    # PYTHON = 'python'
    # JAVASCRIPT = 'javascript'
    # CS = 'c#'
    # CPP = 'cpp'
    #
    # LANGUAGE_CHOICES = (
    #     (PYTHON, 'Python'),
    #     (JAVASCRIPT, 'Javascript'),
    #     (CS, 'C#'),
    #     (CPP, 'C++')
    # )
    name_book = models.CharField(max_length=255, verbose_name='Название книги')
    name_author = models.CharField(max_length=50, verbose_name='Имя автора')
    surname_author = models.CharField(max_length=50, verbose_name='Фамилия автора')
    date_of_publication = models.DateField(auto_now_add=False, auto_now=False)
    publisher = models.CharField(max_length=20, choices=CHOICE_PUBLISHER)
    salary = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return 'Название книги - {0}, Имя Автора - {1}, Фамилия автора - {2}, Дата публикации - {3}, Издатель - {4}, Цена - {5}'.format(
            self.name_book, self.name_author, self.surname_author, self.date_of_publication, self.publisher,
            self.salary)

    def dict(self):
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
