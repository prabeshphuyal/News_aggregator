from django.urls import include, path
from newswebsite.views import news_list, search_query

app_name = 'newswebsite'
urlpatterns = [
    path('', news_list, name='news_list'),
    path('<str:category>/', news_list, name='news_list'),
    path('search', search_query, name='search'),
]