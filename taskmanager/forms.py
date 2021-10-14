from django import forms
from django.forms import fields, widgets,Textarea,TextInput,PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg',"id":"inputName", "placeholder":"Email@mail.com"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg',"id":"inputPassword",'placeholder':"Password"}))

