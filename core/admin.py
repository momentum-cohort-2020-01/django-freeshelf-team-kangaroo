from django.contrib import admin

from .models import Book, Tag, Like


# Register your models here.
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Like)
