from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Author, Library, Librarian, UserProfile
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required, user_passes_test

# Create your views here.
def list_books(request):
    books = Book.objects.get()
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

    def is_admin(user):
    return hasattr(user, 'UserProfile') and user.UserProfile.role == 'Admin'

    @user_passes_test(is_admin)
    def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

    def is_member(user):
    return hasattr(user, 'UserProfile') and user.UserProfile.role == 'Member'

    @user_passes_test(is_member)
    def member_view(request):
    return render(request, 'relationship_app/member_view.html')
    
    def is_librarian(user):
    return hasattr(user, 'UserProfile') and user.UserProfile.role == 'Librarian'

    @user_passes_test(is_librarian)
    def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')















