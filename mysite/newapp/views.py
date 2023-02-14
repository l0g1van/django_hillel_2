from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Avg, Count, FloatField, Max

from newapp.models import Author, Publisher, Book, Store


def view(request):
    return render(request, 'page_1.html')


class AuthorListView(generic.ListView):
    template_name = 'author_list.html'
    context_object_name = 'author_list'
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        context['count'] = context['author_list'].count()
        return context


class PublisherListView(generic.ListView):
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher_list'] = Publisher.objects.all()
        context['publisher_count'] = context['publisher_list'].count()
        return context


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_list'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['book_count'] = context['book_list'].count()
        return context


class StoreListView(generic.ListView):
    template_name = 'store_list.html'
    context_object_name = 'store_list'
    model = Store

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store_list'] = Store.objects.all()
        context['store_count'] = context['store_list'].count()
        return context


def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author_num = Author.objects.all().aggregate(Max('id'))['id__max']
    return render(request, 'author_details.html', {'author': author, 'author_num': author_num})


def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    publisher_num = Publisher.objects.all().count()
    return render(request, 'publisher_details.html', {'publisher': publisher, 'publisher_num': publisher_num})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    authors = book.authors.all()
    avg = Book.objects.all().aggregate(Avg('price', output_field=FloatField()))['price__avg']
    return render(request, 'book_details.html', {'book': book, 'authors': authors, 'avg': avg,
                                                 'num_authors': authors.count()})


def store_details(request, pk):
    store = get_object_or_404(Store, pk=pk)
    books = Store.objects.prefetch_related('books').get(pk=pk).books.all()
    return render(request, 'store_details.html', {'store': store, 'books': books, 'abc': books.count()})
