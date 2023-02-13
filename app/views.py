from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    # data = Book.objects.all()
    # context = {
    #     'data' : data
    # }
    return render(request,'home.html')

def searchBook(request):
    data = Book.objects.all()
    context = {
        'data' : data
    }
    return render(request,'searchBook.html',context)

def aboutUs(request):
    return render(request, 'aboutUs.html')

def contactUs(request):
    return render(request, 'contactUs.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
