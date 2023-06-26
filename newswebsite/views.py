from django.shortcuts import render
from .models import Post 
from rest_framework.response import Response

def news_list(request, category=None):
    if category:
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'news_list.html', context)

def search_query(request):
    query = request.GET.get('search')
    posts = Post.objects.filter(heading__icontains=query) if query else []
    context = {'posts': posts, 'query': query}
    return render(request, 'news_list.html', context)

