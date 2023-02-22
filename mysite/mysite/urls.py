"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from newapp.views import view, AuthorListView, PublisherListView, BookListView, StoreListView, \
    AuthorDetails, StoreDetail, BookDetails, PublisherDetails, BookUpdateView, AuthorUpdateView, \
    PublisherUpdateView, StoreUpdateView, BookDelete, AuthorDelete, PublisherDelete, StoreDelete, BookCreate, \
    AuthorCreate, PublisherCreate, StoreCreate

urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', view, name='index_page'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('pyblisher/', PublisherListView.as_view(), name='publisher_list'),
    path('book/', BookListView.as_view(), name='book_list'),
    path('store/', StoreListView.as_view(), name='store_list'),
    path('author/details/<int:pk>', AuthorDetails.as_view(), name='author_details'),
    path('author/details/<int:pk>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('author/details/<int:pk>/delete', AuthorDelete.as_view(), name='author_delete'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('publisher/details/<int:pk>', PublisherDetails.as_view(), name='publisher_details'),
    path('publisher/details/<int:pk>/update', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher/details/<int:pk>/delete', PublisherDelete.as_view(), name='publisher_delete'),
    path('publisher/create/', PublisherCreate.as_view(), name='publisher_create'),
    path('book/detais/<int:pk>', BookDetails.as_view(), name='book_details'),
    path('book/details/<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('book/details/<int:pk>/delete', BookDelete.as_view(), name='book_delete'),
    path('book/create/', BookCreate.as_view(), name='book_create'),
    path('store/details/<int:pk>', StoreDetail.as_view(), name='store_details'),
    path('store/details/<int:pk>/update', StoreUpdateView.as_view(), name='store_update'),
    path('store/details/<int:pk>/delete', StoreDelete.as_view(), name='store_delete'),
    path('store/create/', StoreCreate.as_view(), name='store_create'),
]
