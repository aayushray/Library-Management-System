from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('searchBook', views.searchBook, name="searchBook"),
    path('aboutUs', views.aboutUs, name="aboutUs"),
    path('contactUs', views.contactUs, name="contactUs"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
]