from django.urls import path
from . import views
from django.shortcuts import render

app_name = "main"

urlpatterns = [
    path('', views.index, name="Index"),
    path('all/news', views.all_news, name="all_news"),
    path('news/<int:pk>', views.single_news_post,
         name="single_post"),
    path('contact', views.contact, name='contact'),
    path('contact-anonym', views.contact_anonym, name='contact_anonym'),
    path("faculty/<int:pk>", views.faculty_view, name="faculty"),
    path("all/best-students", views.best_students, name="best_students"),
    path("best-students/<int:pk>", views.best_student, name="best_student"),
    path('all/resourses', views.all_resourses, name='all_resourses'),
    path('gallery', views.gallery, name='gallery'),
    path('leadership', lambda request: render(
        request, 'main/about_leaders.html'), name='leadership'),
    path('about', lambda request: render(
        request, 'main/about.html'), name='about'),
    path("block-test/", lambda request: render(request, 'main/block-test.html'), name="blok_test")
]
