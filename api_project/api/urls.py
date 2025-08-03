from django.urls import path
from .views import BookListView as BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]