from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="Index"),
    path('news/', views.all_news, name="all_news"),
    path('news/<int:pk>', views.single_news_post, name="single_post")
]
