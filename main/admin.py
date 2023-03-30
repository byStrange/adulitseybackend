from django.contrib import admin
from .models import NewsPost, Person, Faculty, RectorContact, AnonymosContact,  Gallary, GallaryItem

admin.site.register(NewsPost)
admin.site.register(Person)
admin.site.register(Faculty)
admin.site.register(RectorContact)
admin.site.register(AnonymosContact)
admin.site.register(Gallary)
admin.site.register(GallaryItem)
# Register your models here.
