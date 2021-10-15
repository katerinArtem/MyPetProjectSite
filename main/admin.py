from django.contrib import admin
from .models import CustomUser,Post
#from .models import User
# Register your models here.
#admin.site.register(User) 
admin.site.register(CustomUser)
admin.site.register(Post)