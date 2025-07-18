from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Author, Library, Librarian
# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'libraries/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)








