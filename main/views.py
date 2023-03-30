from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'main/index.html')


def all_news(request):
    news = models.NewsPost.objects.all()
    return render(request, 'main/all_news.html', {"news_posts": news})


def single_news_post(request, pk):
    post = models.NewsPost.objects.get(pk=pk)
    return render(request, 'main/news.html', {'post': post})