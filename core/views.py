from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Book
from .forms import BookForm

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'core/books_list.html', {'books': books})




