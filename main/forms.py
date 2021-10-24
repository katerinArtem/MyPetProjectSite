from typing import Optional
from django import forms
from django.db.models.fields import CharField 
from django.forms import widgets,Textarea,TextInput,PasswordInput,ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.translation import gettext, gettext_lazy as _
from .models import CustomUser,Post



class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['user_favicon','username', 'email','first_name','last_name']
        
        
class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','password1','password2']
    