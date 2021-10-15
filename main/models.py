from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50,verbose_name="Автор")
    title = models.CharField(max_length=255,verbose_name="Название")
    content = models.TextField(verbose_name="Контент")
    date_created = models.DateTimeField(auto_now_add = True,verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password = None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("username is required")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
     
    def create_superuser(self,email,username,password = None):
        user = self.create_user(email,username,password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50,verbose_name="Имя пользователя")
    email = models.EmailField(unique=True,max_length=50,verbose_name="Аддрес электронной почты")
    first_name = models.CharField(max_length=50,verbose_name="Имя")
    last_name = models.CharField(max_length=50,verbose_name="Фамилия")
    date_joined = models.DateTimeField(auto_now_add = True,verbose_name="Дата регистрации")
    last_login = models.DateTimeField(auto_now=True,verbose_name="ПОследнии вход")
    is_admin = models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self ,perm , obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        


