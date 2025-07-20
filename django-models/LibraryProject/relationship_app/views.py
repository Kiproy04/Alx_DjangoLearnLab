from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Author, Library, Librarian
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    author = Author.objects.filter(Book)
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = Library.books.all()
        context['list_books'] = library.list_books()

class UserCreationForm():
    template_name = 'relationship_app/register.html'
    
@user_passes_test
class AdminDetailView():

class MemberDetailView():

class LibrarianDetailView():









