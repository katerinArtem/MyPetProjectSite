"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django import contrib
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path,include
from django.views.generic.base import View 
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from . import settings
from django.conf.urls.static import static
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register('posts', views.PostView, 'posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('main.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',LoginView.as_view(template_name="login.html",authentication_form=LoginForm),name='_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
