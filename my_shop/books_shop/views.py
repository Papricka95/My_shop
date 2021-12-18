from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView


class MainView(TemplateView):
    template_name = 'main_page.html'
    ctx = {}

    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)


class RegisterFormView(FormView):
    template_name = 'register.html'  # что отобразить пользователю с нашей формой
    # form_class = UserCreateForm
    success_url = '/books_shop/login'  # этот урл будет срабатывать в случае успешной регистрации

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

# save views as function for some time (their need do as class after some time)
# def main_page(request):
#     return HttpResponse('Приветствую вас в моем магазине! Скоро он откроется!')
