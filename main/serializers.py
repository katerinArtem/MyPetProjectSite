from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import CustomUser,Post,Message

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'last_login',
            'user_favicon',
            'is_admin',
            'is_active',
            'is_stuff',
            'is_superuser')
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'authorkey',
            'author',
            'title',
            'content',
            'date_created',
        )
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'text',
            'author',
            'addressee',
            'date_created',
        )