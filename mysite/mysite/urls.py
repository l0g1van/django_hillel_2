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

from newapp.views import view, author_details, AuthorListView, PublisherListView, BookListView, StoreListView, \
    publisher_details, book_details, store_details

urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', view, name='index_page'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('pyblisher/', PublisherListView.as_view(), name='publisher_list'),
    path('book/', BookListView.as_view(), name='book_list'),
    path('store/', StoreListView.as_view(), name='store_list'),
    path('author/details/<int:pk>', author_details, name='author_details'),
    path('publisher/details/<int:pk>', publisher_details, name='publisher_details'),
    path('book/detais/<int:pk>', book_details, name='book_details'),
    path('store/details/<int:pk>', store_details, name='store_details')
]
