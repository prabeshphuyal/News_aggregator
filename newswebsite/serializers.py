from rest_framework import serializers
from newswebsite.models import Post,CATEGORY_CHOICES
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
        class Meta:
                model = Post
                fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
        post =serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
        class Meta:
                model = User
                fields =['id','username','post']