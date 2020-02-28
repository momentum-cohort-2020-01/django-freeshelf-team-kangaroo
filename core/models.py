from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    url = models.URLField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100, null=True)
    tags = TaggableManager()

    def __str__(self):

        return f"Book title {self.title} Author {self.author}  Url {self.url} Description {self.description} tag{self.tags}"


class Tag(models.Model):
    name = models.CharField(max_length = 40)
    slug = slugify(name)

