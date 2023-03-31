from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from . import forms 


def index(request):
    news_posts = models.NewsPost.objects.all()
    return render(request, 'main/index.html', {"news_posts": news_posts})


def all_news(request):
    news = models.NewsPost.objects.all()
    return render(request, 'main/all_news.html', {"news_posts": news})


def single_news_post(request, pk):
    post = models.NewsPost.objects.get(pk=pk)
    print(dir(post))
    return render(request, 'main/news.html', {'post': post})


def contact(request):
    if request.method == 'POST':
        contactForm = forms.RectorContactForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            messages.success(request, 'Sizning murojaatingiz qabul qilindi')
        else:
            messages.error(request, 'Xatolik yuz berdi')
            return redirect('main:contact')
    return render(request, 'main/contact.html')


def contact_anonym(request):
    if request.method == 'POST':
        print(request.POST)
        models.AnonymousContact.objects.create(
            text=request.POST['text'],
            name=request.POST['name'],
            phone_num_or_username=request.POST['phone_num_or_username'],
            email=request.POST['email']
        )
        messages.success(request, 'Sizning murojaatingiz qabul qilindi')
    return render(request, 'main/anonymous-contact.html')
