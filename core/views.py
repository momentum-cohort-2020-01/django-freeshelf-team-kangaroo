from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Book
from .forms import BookForm

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'core/books_list.html', {'books': books})

def books_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "core/books_details.html", {'book': book, 'pk':pk})


def books_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect('books-details', pk=note.pk)
    else:
        form = BookForm(instance = book)
        return render(request, 'core/books_edit.html', {"form": form})

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

   
   





