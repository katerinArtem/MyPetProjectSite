from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm,UserUpdateForm,NewPostForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Post,CustomUser
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):
    return HttpResponse("Hello world!")

def home(request):
    return render(request,'main/home.html')

def features(request):
    return render(request,'main/features.html')


def public_profile(request,id):

    public_user = CustomUser.objects.filter(id = id).first() 

    context = {
        'posts_count':Post.objects.filter(authorkey = public_user).__len__(),
        'public_user':public_user
    }

    return render(request,'public_profile.html',context)

@login_required
def update_post(request,id):
    obj = Post.objects.filter(id = id)

    if request.method == 'POST':
        form = NewPostForm(request.POST,instance=obj.first())
        if form.is_valid():
            form.save()
            messages.success(request,"Update successful.")
            return profile_posts(request)
        messages.error(request, "Unsuccessful update")

    form = NewPostForm(instance=obj.first())
    form.fields['title'].widget.attrs = {'class':'form-control','id':'inputTitle'}
    form.fields['content'].widget.attrs = {'class':'form-control','id':'inputContent'}

    context = {
        'update_id':id,
        'form':form
    }

    return profile_posts(request,context)

@login_required
def delete_post(request,id):
    obj = Post.objects.filter(id = id)
    obj.delete()
    return redirect('main:profile_posts')

@login_required
def profile_posts(request,context={}):
    posts = Post.objects.filter(author = request.user.username).order_by('-id')
    posts_paginator = Paginator(posts,6)
    page_num = request.GET.get('page',1)
    page = posts_paginator.get_page(page_num)

    context.update({
        'page':page,
    })
    return render(request,'main/profile_posts.html',context)

@login_required
def posts(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.authorkey = request.user
            post.author = request.user.username
            post.save()
            messages.success(request, "Post added successful." )
            return redirect('main:posts')
        messages.error(request, "Post doun't  added. Invalid information.")
    form = NewPostForm()
    form.fields['title'].widget.attrs = {
        'class':'form-control','id':'inputTitle','placeholder':'title'
    }
    form.fields['content'].widget.attrs = {
        'class':'form-control','id':'inputContent','placeholder':'content'
    }
    posts = Post.objects.all().order_by('-id')
    posts_paginator = Paginator(posts,6)
    page_num = request.GET.get('page',1)
    page = posts_paginator.get_page(page_num)

    context = {
        'form':form,
        'page':page
    }

    return render(request,'main/posts.html',context)

def sign_up(request):
    if request.method == "POST":
	    form = NewUserForm(request.POST)
	    if form.is_valid():
		    user = form.save()
		    login(request, user)
		    messages.success(request, "Registration successful." )
		    return redirect("main:home")
	    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    form.fields['username'].widget.attrs = {
        'class': 'form-control',"id":"inputName", "placeholder":"Username"}
    form.fields['email'].widget.attrs = {
        'class': 'form-control','id':'inputEmail','placeholder':'Email@gmail.com'
    }
    form.fields['first_name'].widget.attrs = {
        'class': 'form-control','id':'inputFirstName','placeholder':'First Name'        
    }
    form.fields['last_name'].widget.attrs = {
        'class': 'form-control','id':'inputLastName','placeholder':'Last Name'        
    }
    form.fields['password1'].widget.attrs = {
        'class': 'form-control','id':'inputPassword1'
    }
    form.fields['password2'].widget.attrs = {
        'class': 'form-control','id':'inputPassword2'
    }
    return render (request=request, template_name="sign_up.html", context={"form":form})

@login_required
def profile_update(request):
    user = request.user
    if (request.method == 'POST'):
        form = UserUpdateForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Update successful.")
            return redirect("main:profile_update")
        messages.error(request, "Unsuccessful update")
    form = UserUpdateForm(instance=user)
    form.fields['username'].widget.attrs = {
        'class': 'form-control','id':'inputUserName','placeholder':user.username        
    }
    form.fields['email'].widget.attrs = {
        'class': 'form-control','id':'inputEmail','placeholder':user.email        
    }
    form.fields['first_name'].widget.attrs = {
        'class': 'form-control','id':'inputFirstName','placeholder':user.first_name        
    }
    form.fields['last_name'].widget.attrs = {
        'class': 'form-control','id':'inputLastName','placeholder':user.last_name        
    }
    return render(request = request,template_name='profile.html',context={'form':form})


