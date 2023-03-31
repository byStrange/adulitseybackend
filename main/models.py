from django.db import models
from django_quill.fields import QuillField

# Create your models here.


class NewsPost(models.Model):
    NEWS_TYPE_CHOICES = (
        ('primary', 'Video'),
        ('secondary', 'Foto'),
        ('triary', 'Qonunchilik'),
    )
    title = models.CharField(max_length=255)
    little_image = models.ImageField(upload_to="media/news_post/")
    big_image = models.ImageField(upload_to='media/news_post/')
    news_type = models.CharField(choices=NEWS_TYPE_CHOICES, max_length=255)
    body = QuillField()

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media/person_pictures')
    phone_number = models.CharField(max_length=255)
    biography = QuillField()

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Faculties'


class RectorContact(models.Model):
    STATUS_CHOICES = (
        ('Jismoniy shaxs', 'js'),
        ('Yuridik shaxs', 'ys')
    )

    CONTACT_TYPE_CHOICES = (
        ('Murojaat', 'm'),
        ('Shikoyat', 'sh'),
        ('Taklif', 't')
    )
    summary = models.CharField(max_length=500)
    text = models.TextField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_num_or_username = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)
    contact_type = models.CharField(
        choices=CONTACT_TYPE_CHOICES, max_length=255)

    def __str__(self):
        return self.name


class AnonymousContact(models.Model):
    text = models.TextField()
    name = models.CharField(null=True, blank=True, max_length=255)
    phone_num_or_username = models.CharField(
        null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    image = models.ImageField(upload_to='media/gallery')
    summary = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    items = models.ManyToManyField(GalleryItem)

    def __str__(self):
        return self.items.__len__()

    class Meta:
        verbose_name_plural = 'Gallaries'
