from django.contrib import admin
from .models import Author, Book, PublishingHouse
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(PublishingHouse)
