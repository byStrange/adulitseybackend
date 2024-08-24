from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from . import forms


def index(request):
    news_posts = models.NewsPost.objects.all()
    video_posts = models.NewsPost.objects.filter(news_type="primary")
    photo_posts =  models.NewsPost.objects.filter(news_type="secondary")
    legislation_posts = models.NewsPost.objects.filter(news_type="triary")
    best_students_posts = models.NewsPost.objects.filter(news_type="best_student")

    useful_resources = models.UsefulResources.objects.all()
    faculties = models.Faculty.objects.all()

    objects = {
        "news_posts": news_posts,
        "primary": video_posts,
        "secondary": photo_posts,
        "triary":legislation_posts,
        "useful_resources": useful_resources,
        "talanted_students": best_students_posts,
        "faculties": faculties
    }
    return render(request, 'main/index.html', objects)


def all_news(request):
    news_type = request.GET.get('type')
    news = models.NewsPost.objects.all()
    if news_type:
        news = news.filter(news_type=news_type)
    return render(request, 'main/all_news.html', {"news_posts": news})


def all_resourses(request):
    resourses = models.UsefulResources.objects.all()
    return render(request, 'main/all_resourses.html', {'resourses': resourses})


def single_news_post(request, pk):
    post = models.NewsPost.objects.get(pk=pk)
    print(dir(post))
    return render(request, 'main/news.html', {'post': post})


def contact(request):
    if request.method == 'POST':
        contactForm = forms.RectorContactForm(request.POST)
        print(contactForm.errors)
        if contactForm.is_valid():
            print(contactForm.cleaned_data, 'cleaned data')
            contactForm.save()
            messages.success(request, 'Sizning murojaatingiz qabul qilindi')
        else:
            print(contactForm.errors, 'Xatolik yuz berdi')
            messages.error(request, 'Xatolik yuz berdi')
            return redirect('main:contact')
    return render(request, 'main/contact.html')


def contact_anonym(request):
    if request.method == 'POST':
        print(request.POST)
        contactForm = forms.AnonymousContactForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            messages.success(request, 'Sizning murojaatingiz qabul qilindi')
        else:
            print(contactForm.errors)
    return render(request, 'main/anonymous-contact.html')


def faculty_view(request, pk):
    faculty = models.Faculty.objects.get(pk=pk)
    return render(request, 'main/faculty.html', {"faculty": faculty})


def best_students(request):
    students = models.NewsPost.objects.filter(news_type="best_student")
    return render(request, 'main/best_students.html', {"students": students})


def best_student(request, pk):
    students = models.NewsPost.objects.get(news_type="best_student", pk=pk)
    return render(request, 'main/best_student.html', {"student": student})


def gallery(request):
    gallery = models.Gallery.objects.first()
    return render(request, 'main/gallery.html', {"gallery": gallery})


def leadership(request):
    return render(request, 'main/rahbariyat.html')
