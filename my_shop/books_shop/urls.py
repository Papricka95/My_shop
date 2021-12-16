from django.urls import path

from books_shop import views

urlpatterns = [
    # url(r'^$', views.MainView.as_view()),
    path('/', views.main_page),
]
