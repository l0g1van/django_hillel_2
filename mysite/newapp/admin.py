from django.contrib import admin
from newapp.models import Author, Publisher, Book, Store


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']

    fieldsets = [
        (None, {'fields': ['name', 'age']})]

    list_filter = ['age']

    search_fields = ['name']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']

    list_filter = ['name']

    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pubdate', 'rating']

    fieldsets = [
        (None, {'fields': ['name', 'pubdate']}),
        ('Pages, Price and Rating', {'fields': ['pages', 'price', 'rating'], 'classes': ['collapse']})
    ]

    list_filter = ['pubdate', 'rating']

    search_fields = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

    list_filter = ['name']
    search_fields = ['name']


