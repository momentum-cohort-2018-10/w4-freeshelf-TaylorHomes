import csv, io
from django.shortcuts import render
from collection.models import Book
# double check path!!


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books,
    })

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'templates/index_html', {
        'book': book,
    })


def book_upload(request):
    template = "base.html"

