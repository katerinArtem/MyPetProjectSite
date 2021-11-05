from collections import namedtuple
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('react/',views.index,name='react'),
    path('',views.home,name = 'home'),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('profile/update/',views.profile_update,name = 'profile_update'),
    path('Posts/',views.posts,name = 'posts'),
    path('features/',views.features,name = 'features'),
    path('profile/posts/',views.profile_posts,name = 'profile_posts'),
    path('profile/posts/delete/<int:id>',views.delete_post,name='delete_post'),
    path('profile/posts/update/<int:id>',views.update_post,name='update_post'),
    path('profile/public/<int:id>',views.public_profile,name='public_profile'),
    path('profile/dialogs/',views.profile_dialogs,name='profile_dialogs'),
    path('profile/dialog/',views.profile_dialog,name="profile_dialog"),
]