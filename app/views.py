from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User Successfully Registered')
            return HttpResponseRedirect('login')
        else:
            return render(request,'register.html', {'form':form})
    
    else:
        form = RegistrationForm
        return render(request, 'register.html',{'form':form})

def login(request):
    # form = LoginForm()
    # if request.method == 'POST':
    #     form = LoginForm(request.POST or None)
    #     if form.is_valid():
    #         print("hii")
    #         uname = form.cleaned_data['username']
    #         upass = form.cleaned_data['password']
    #         try:
    #             user = User.objects.get(username=uname)
    #             if user.check_password(upass):
    #                 messages.success(request, 'Logged in Successfully')
    #                 return HttpResponseRedirect('home')
    #         except:
    #             messages.error(request, 'Invalid Username or Password')
    #             return HttpResponseRedirect('login')
    #     else:
    #         return render(request,'login.html', {'form':form})
    return render(request,'login.html', {'form':form})
