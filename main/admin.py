from django.contrib import admin
from .models import NewsPost, Person, Faculty, RectorContact, AnonymousContact,  Gallery, GalleryItem,  TalentedStudent, UsefulResources

admin.site.register(NewsPost)
admin.site.register(Person)
admin.site.register(Faculty)
admin.site.register(RectorContact)
admin.site.register(AnonymousContact)
admin.site.register(Gallery)
admin.site.register(TalentedStudent)
admin.site.register(UsefulResources)
admin.site.register(GalleryItem)
