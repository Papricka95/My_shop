from django.urls import path, re_path

from books_shop import views

urlpatterns = [
    # url(r'^$', views.MainView.as_view()),
    path('', views.MainView.as_view()),
    re_path('register/$', views.RegisterFormView.as_view()),
    re_path('login/$', views.LoginFormView.as_view()),
    # re_path('logout/$', views.LogoutFormView.as_view()),

]
