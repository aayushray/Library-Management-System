from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import *

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required='True',widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email',}
    
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class VisitorForm(ModelForm):
    full_name = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Address',widget=forms.TextInput(attrs={'class':'form-control'}))
    name_of_institution = forms.CharField(label='Name of Institution',widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth = forms.CharField(label='Date Of Birth',widget=forms.DateInput(attrs={'class':'form-control'}))
    class Meta:
        model = Visitor
        fields = ['full_name','address','name_of_institution','date_of_birth']