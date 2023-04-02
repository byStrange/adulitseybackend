from django.db import models
from django_quill.fields import QuillField
from multiselectfield import MultiSelectField

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
    video = models.FileField(upload_to='media/news_post/', blank=True, null=True)
    news_type = models.CharField(choices=NEWS_TYPE_CHOICES, max_length=255)
    body = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)

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

class TalentedStudent(models.Model):
    fullname = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media/talented_students')
    phone_number = models.CharField(max_length=255)
    biography = QuillField()

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Talented Students'


class RectorContact(models.Model):
    STATUS_CHOICES = (
        ('js', 'Jismoniy shaxs'),
        ('ys', 'Yuridik shaxs')

    )

    CONTACT_TYPE_CHOICES = (
        ('m', 'Murojaat'),
        ('sh', 'Shikoyat'),
        ('t', 'Taklif')
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
    CHOICES = (
        ('grid-item--width2', 'uzunlik 2'),
        ('grid-item--width3', 'uzunlik 3'),
        ('grid-item--height2', 'balandlik 2'),
        ('grid-item--height3', 'balandlik 3'),
    )
    image = models.ImageField(upload_to='media/gallery')
    summary = models.CharField(max_length=255)
    size = MultiSelectField(choices=CHOICES, max_length=255, max_choices=3, blank=True, null=True)

    def __str__(self):
        return self.summary 


class Gallery(models.Model):
    items = models.ManyToManyField(GalleryItem)

    def __str__(self):
        return str(self.items.count())

    class Meta:
        verbose_name_plural = 'Gallaries'


class UsefulResources(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/useful_resources')
    img = models.ImageField(upload_to='media/useful_resources', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    summary = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Useful Resources'
