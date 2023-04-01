from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from . import forms


def index(request):
    news_posts = models.NewsPost.objects.all()
    primary, secondary, triatery = [], [], []
    for post in news_posts:
        if post.news_type == 'primary':
            primary.append(post)
        elif post.news_type == 'secondary':
            secondary.append(post)
        elif post.news_type == 'triary':
            triatery.append(post)

    useful_resources = models.UsefulResources.objects.all()
    talanted_students = models.TalentedStudent.objects.all()
    faculties = models.Faculty.objects.all()

    for i in talanted_students:
        print(i)

    objects = {
        "news_posts": news_posts,
        "primary": primary,
        "secondary": secondary,
        "triary": triatery,
        "useful_resources": useful_resources,
        "talanted_students": talanted_students,
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
    students = models.TalentedStudent.objects.all()
    return render(request, 'main/best_students.html', {"students": students})


def best_student(request, pk):
    student = models.TalentedStudent.objects.get(pk=pk)
    return render(request, 'main/best_student.html', {"student": student})
