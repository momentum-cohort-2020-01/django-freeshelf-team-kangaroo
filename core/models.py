from django.contrib.auth.models import User
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
    like = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

   

    def __str__(self):

        return f"Book title {self.title} Author {self.author}  Url {self.url} Description {self.description} tag{self.tag}"

    def get_absolute_url(self):
        return reverse('books_details', kwargs={'slug': self.slug})

class Tag(models.Model):
    name = models.CharField(max_length = 40)
 #trying to add slug
    slug = models.SlugField(null=False, unique=True, default=slugify(name))
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Like(models.Model):
    liker = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="likes", on_delete=models.CASCADE)

    def __str__(self):
        return f"Liker: {self.liker}, Book: {self.book}"
