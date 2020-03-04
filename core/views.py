from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Book, Tag, Like, User
from .forms import BookForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required()
def books_list(request):
    books = Book.objects.all()
    likes = get_user_likes(request)
    return render(request, 'core/books_list.html', {'books': books, 'likes': likes})

def books_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    liked_by = [like.liker.username for like in book.likes.all()]
    count = book.likes.all().count()
    return render(request, "core/books_details.html", {'book': book, 'pk':pk, 'liked_by': liked_by, 'count': count})


def books_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('books-details', book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'core/books_edit.html', {'form': form})

def books_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect('books-list')
    else:
        form = BookForm()
    return render(request, 'core/books_edit.html', {'form': form})

def books_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books-list')

def tagged(request, slug): 
    # Filter books by tag name  
    tag = Tag.objects.get(slug=slug)
    books = Book.objects.filter(tag=tag)
    return render(request, 'core/books_list.html', {'tag': tag, 'books': books})

def get_user_likes(request):
    user = User.objects.get(username=request.user.username)
    likes = [like.book for like in user.likes.all()]
    return likes

def books_liked(request, pk):
    user = User.objects.get(username=request.user.username)
    book = Book.objects.get(pk=pk)
    like = Like(liker=user , book=book)
    like.save()
    return redirect('books-list')

def books_disliked(request, pk):
    user = User.objects.get(username=request.user.username)
    book = Book.objects.get(pk=pk)
    like = Like.objects.filter(liker=user, book=book)
    like[0].delete()
    return redirect('books-list')
    
    