from django.db import models
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    url = models.URLField(max_length = 200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return f"Book title {self.title} Author {self.author}  Url {self.url} Description {self.description} tag{self.tag}"


class Tag(models.Model):
    name = models.CharField(max_length = 40)
    slug = slugify(name)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

