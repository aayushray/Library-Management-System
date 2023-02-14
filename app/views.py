from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def searchBook(request):
    data = Book.objects.filter(is_issued = False)
    # print(data)
    context = {
        'data' : data
    }
    return render(request,'viewBook.html',context)

def issueBook(request):
    return render(request, 'issueBook.html')

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
    return render(request,'login.html')

def profile(request):
    data = Visitor.objects.all()
    context = {
        'data' : data
    }
    # print(context)
    return render(request, 'profile.html', context)
