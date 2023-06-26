from django.db import router
from django.urls import include, path
from newswebsite.views import news_list, search_query
from .api import PostListAPIView, PostDetailAPIView
app_name = 'newswebsite'
urlpatterns = [
    path('', news_list, name='news_list'),
    path('<str:category>/', news_list, name='news_list'),
    path('search', search_query, name='search'),
    path('api/posts/', PostListAPIView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    
]
