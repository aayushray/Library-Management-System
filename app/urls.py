from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    path('', views.home, name="home"),
    
    path('searchBook', views.searchBook, name="searchBook"),
    path('issueBook', views.issueBook, name="issueBook"),

    path('aboutUs', views.aboutUs, name="aboutUs"),
    path('contactUs', views.contactUs, name="contactUs"),

    path('register', views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name="login.html",
    authentication_form=LoginForm), name="login"),
    path('logout',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('profile', views.profile, name="profile")

]