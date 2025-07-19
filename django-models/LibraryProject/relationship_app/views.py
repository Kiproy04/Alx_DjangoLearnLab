from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Author, Librarian
from .models import Library
# Create your views here.
def get_list_books(request):
    books = Book.objects.all()
    author = Author.objects.filter(Book)
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = Library.get.all()
        context['list_books'] = library.get_list_books()








