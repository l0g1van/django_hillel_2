from django.shortcuts import render, get_object_or_404
from django.views import generic

from newapp.models import Author, Publisher, Book, Store


def view(request):
    return render(request, 'page_1.html')


class AuthorListView(generic.ListView):
    template_name = 'author_list.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.all()


class PublisherListView(generic.ListView):
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'

    def get_queryset(self):
        return Publisher.objects.all()


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.all()


class StoreListView(generic.ListView):
    template_name = 'store_list.html'
    context_object_name = 'store_list'

    def get_queryset(self):
        return Store.objects.all()


def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_details.html', {'author': author})


def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'publisher_details.html', {'publisher': publisher})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # get_object_or_404(Book, pk=pk).publisher.name
    authors = book.authors.all()
    return render(request, 'book_details.html', {'book': book, 'authors': authors})


def store_details(request, pk):
    store = get_object_or_404(Store, pk=pk)
    books = Store.objects.prefetch_related('books').get(pk=pk).books.all()
    return render(request, 'store_details.html', {'store': store, 'books': books})
