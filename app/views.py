from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def searchBook(request):
    data = Book.objects.filter(is_issued = False)
    context = {
        'data' : data
    }
    return render(request,'viewBook.html',context)

def issueBook(request):
    if request.user.is_authenticated:
        student = Visitor.objects.filter(user = request.user).get()
        data = Book.objects.filter(is_issued = False)  

        print(student)
        context = {
            'data' : data
        }

        if 'book_issued' in request.POST:
            if student.number_of_books >= 2:
                messages.error(request, 'ERROR: You have already Issued 2 books!!')
                return HttpResponseRedirect('issueBook')

            else:
                if request.method == 'POST':
                    bookName = request.POST.get('bookName')
                    book = Book.objects.get(book_name = bookName)
                    book.is_issued = True
                    book.save()

                    student.number_of_books+=1
                    student.save()
                    print(student.number_of_books)
                    messages.success(request, 'Book Issued Successfully')
                    return HttpResponseRedirect('issueBook')

        else:
            return render(request,'issuebook.html', context)
    
    else:
        return HttpResponseRedirect('login')

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
            return redirect('login')
        else:
            return render(request,'register.html', {'form':form})
    
    else:
        form = RegistrationForm
        return render(request, 'register.html',{'form':form})

def login(request):
    return render(request,'login.html')

def profile(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('home')
        else:
            return render(request,'profile.html', {'form':form})
    
    else:
        form = VisitorForm
        return render(request, 'profile.html',{'form':form})