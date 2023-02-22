from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

from newapp.models import Author, Publisher, Book, Store


def view(request):
    return render(request, 'page_1.html')


class AuthorListView(generic.ListView):
    template_name = 'author_list.html'
    context_object_name = 'author_list'
    paginate_by = 50
    model = Author

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author_list'] = Author.objects.all()
    #     # context['count'] = context['author_list'].count()
    #    context['count'] = Author.objects.prefetch_related('books').annotate(books_count=Count('books'))[0].books_count
    #
    #     return context


class PublisherListView(generic.ListView):
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'
    paginate_by = 50
    model = Publisher

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['publisher_list'] = Publisher.objects.all()
    #     # context['publisher_count'] = context['publisher_list'].count()
    #     context['count'] = \
    #         Publisher.objects.prefetch_related('books').annotate(books_count=Count('books'))[0].books_count
    #
    #     return context


class BookListView(generic.ListView):
    model = Book
    paginate_by = 50
    template_name = 'book_list.html'
    context_object_name = 'book_list'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book_list'] = Book.objects.all()
    #     # context['publisher'] = Book.objects.select_related('publisher').all()
    #     # context['book_count'] = context['book_list'].count()
    #     return context


class StoreListView(generic.ListView):
    template_name = 'store_list.html'
    context_object_name = 'store_list'
    paginate_by = 50
    model = Store

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['store_list'] = Store.objects.all()
    #     # context['store_count'] = context['store_list'].count()
    #     return context


# def author_details(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     author_num = Author.objects.all().aggregate(Max('id'))['id__max']
#     return render(request, 'author_details.html', {'author': author, 'author_num': author_num})


class AuthorDetails(generic.DetailView):
    model = Author
    template_name = 'author_details.html'


# def publisher_details(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     avg_price_of_published_books = Publisher.objects.annotate(Avg('books__price')).filter(pk=pk)[0].books__price__avg
#     return render(request, 'publisher_details.html', {'publisher': publisher,
#                                                       'avg_price_of_published_books': avg_price_of_published_books})


class PublisherDetails(generic.DetailView):
    model = Publisher
    template_name = 'publisher_details.html'
    queryset = Publisher.objects.prefetch_related('books').annotate(books_count=Count('books'))


# def book_details(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'book_details.html', {'book': book})


class BookDetails(generic.DetailView):
    model = Book
    template_name = 'book_details.html'


# def store_details(request, pk):
#     store = get_object_or_404(Store, pk=pk)
#     return render(request, 'store_details.html', {'store': store})


class StoreDetail(generic.DetailView):
    model = Store
    template_name = 'store_details.html'


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['name', 'price', 'rating', 'pubdate', 'publisher']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class AuthorUpdateView(generic.UpdateView):
    model = Author
    fields = ['name', 'age']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class PublisherUpdateView(generic.UpdateView):
    model = Publisher
    fields = ['name']
    template_name = 'publisher_form.html'
    success_url = reverse_lazy('publisher_list')


class StoreUpdateView(generic.UpdateView):
    model = Store
    fields = ['name']
    template_name = 'store_form.html'
    success_url = reverse_lazy('store_list')


class BookDelete(LoginRequiredMixin, generic.DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')
    template_name = 'book_confirm_delete.html'

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(BookDelete, self).form_valid(form)


class AuthorDelete(generic.DeleteView):
    model = Author
    context_object_name = 'author'
    success_url = reverse_lazy('author_list')
    template_name = 'author_confirm_delete.html'

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(AuthorDelete, self).form_valid(form)


class PublisherDelete(generic.DeleteView):
    model = Publisher
    context_object_name = 'publisher'
    success_url = reverse_lazy('publisher_list')
    template_name = 'publisher_confirm_delete.html'

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(PublisherDelete, self).form_valid(form)


class StoreDelete(generic.DeleteView):
    model = Store
    context_object_name = 'store'
    success_url = reverse_lazy('store_list')
    template_name = 'store_confirm_delete.html'

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(StoreDelete, self).form_valid(form)


class BookCreate(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['name', 'price', 'rating', 'pubdate', 'publisher', 'authors']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class AuthorCreate(generic.CreateView):
    model = Author
    fields = ['name', 'age']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class PublisherCreate(generic.CreateView):
    model = Publisher
    fields = ['name']
    template_name = 'publisher_form.html'
    success_url = reverse_lazy('publisher_list')


class StoreCreate(generic.CreateView):
    model = Store
    fields = ['name', 'books']
    template_name = 'store_form.html'
    success_url = reverse_lazy('store_list')


