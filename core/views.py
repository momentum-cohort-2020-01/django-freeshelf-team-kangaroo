from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Book
from .forms import BookForm

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'core/books_list.html', {'books': books})

def books_edit(request, pk):
    books = get_object_or_404(Book, pk=pk)
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




