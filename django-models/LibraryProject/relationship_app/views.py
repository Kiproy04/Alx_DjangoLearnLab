from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Author, Librarian, UserProfile, User
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object(pk=pk)
        context ['list_books'] = library.list_books()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginView:
    template_name = 'relationship_app/login.html'

class LogoutView:
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('admin')  
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



















