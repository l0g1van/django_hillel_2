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
        # context['count'] = context['author_list'].count()
        context['count'] = Author.objects.prefetch_related('books').annotate(books_count=Count('books'))[0].books_count

        return context


class PublisherListView(generic.ListView):
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher_list'] = Publisher.objects.all()
        # context['publisher_count'] = context['publisher_list'].count()
        context['count'] = \
            Publisher.objects.prefetch_related('books').annotate(books_count=Count('books'))[0].books_count

        return context


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_list'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        # context['publisher'] = Book.objects.select_related('publisher').all()
        # context['book_count'] = context['book_list'].count()
        return context


class StoreListView(generic.ListView):
    template_name = 'store_list.html'
    context_object_name = 'store_list'
    model = Store

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store_list'] = Store.objects.all()
        # context['store_count'] = context['store_list'].count()
        return context


def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author_num = Author.objects.all().aggregate(Max('id'))['id__max']
    return render(request, 'author_details.html', {'author': author, 'author_num': author_num})


def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    avg_price_of_published_books = Publisher.objects.annotate(Avg('books__price')).filter(pk=pk)[0].books__price__avg
    return render(request, 'publisher_details.html', {'publisher': publisher,
                                                      'avg_price_of_published_books': avg_price_of_published_books})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_details.html', {'book': book})


def store_details(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'store_details.html', {'store': store})
