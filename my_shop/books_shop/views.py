from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from books_shop.forms import BookForm
from books_shop.models import Book


class MainView(TemplateView):
    template_name = 'main_page.html'
    book_form = BookForm

    def get(self, request, **kwargs):
        ctx = {}
        # тут должна быть проверка пользователя на авторизованность на сайте
        # и только после этого будет показываться все данные. Но пока оставим так
        all_books = Book.objects.all() # Считываем все книги, которые хранятся в БД
        ctx['books'] = all_books
        ctx['books_form'] = self.book_form # Перекидываем форму, которая будет отображаться пользователю в шаблоне
        return render(request, self.template_name, ctx)
        # return JsonResponse({'Response': true})


class RegisterFormView(FormView):
    template_name = 'register.html'  # что отобразить пользователю с нашей формой
    # form_class = UserCreateForm
    success_url = '/books_shop/login'  # этот урл будет срабатывать в случае успешной регистрации

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/books-shop/'

    # валидация формы
    def form_valid(self, form):
        # получаем пользователя на основе введенных в форму данных
        self.user = form.get_user()
        # логиним user
        login(self.request, self.user)
        # возвращаем метод предка LoginFormView form_valid
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)

# save views as function for some time (their need do as class after some time)
# def main_page(request):
#     return HttpResponse('Приветствую вас в моем магазине! Скоро он откроется!')
