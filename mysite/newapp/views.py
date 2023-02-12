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
    return render(request, 'author_details.html', {'author': author, 'books': author.book_set.all()})
                  # context={'name': author.name, 'age': author.age, 'books': author.book_set.all()})

