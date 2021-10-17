from collections import namedtuple
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.home,name = 'home'),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('profile/update',views.profile_update,name = 'profile_update'),
    path('Posts/',views.posts,name = 'posts'),
    path('features/',views.features,name = 'features'),
    path('profile/posts',views.profile_posts,name = 'profile_posts'),
]