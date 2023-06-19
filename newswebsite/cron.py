from urllib.parse import urlparse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Post, CATEGORY_CHOICES

def my_cron_job():
    national = 'https://kathmandupost.com/national'
    politics = "https://kathmandupost.com/politics"
    valley = "https://kathmandupost.com/valley"
    opinion = "https://kathmandupost.com/opinion"
    money="https://kathmandupost.com/money"
    sports = "https://kathmandupost.com/sports"
    culture  = "https://kathmandupost.com/art-culture"
    url_list = [national,politics,valley,opinion,money,sports,culture]
    for link in url_list:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', {'class':'article-image'})
        main_url, category = get_category_and_main_url(link)
        for article in articles:
            if not article.find('h3') or not article.find('p'):
                continue
            heading = article.find('h3').get_text()
            image= ""
            if article.find('img',{'class': 'img-responsive'}):
                image = article.find('img')['data-src']

            content = article.find('p').get_text()
            url ="https://"+main_url+'/'+article.find('a').get('href')

            if Post.objects.filter(heading=heading).exists():
                continue
            Post.objects.create(**{
                    'heading': heading,
                    'image': image,
                    'content': content,
                    'category': category,
                    'url': url
            })
        
def get_category_and_main_url(url):
    default_category= [choice[0] for choice in CATEGORY_CHOICES]
    url_parse = urlparse(url)
    main_url = url_parse.netloc
    category = url_parse.path.replace("/","")
    if  category not in default_category:
        category = 'others'
    return main_url,category
