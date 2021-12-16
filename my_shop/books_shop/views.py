from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


# class MainView(TemplateView):
#     template_name = 'main_page.html'
#     books_form = BookForm
#
#     def get(self, request):
#         ctx = {}
#
def main_page(request):
    return HttpResponse('Приветствую вас в моем магазине! Скоро он откроется!')
