from rest_framework import serializers
from newswebsite.models import Post,CATEGORY_CHOICES

class PostSerializer(serializers.ModelSerializer):
        class Meta:
                model = Post
                fields ='__all__'