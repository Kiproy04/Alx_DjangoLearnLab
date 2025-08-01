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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
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
            return redirect('UserCreationForm')  
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.UserProfile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.is_authenticated and user.UserProfile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.UserProfile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@login_required 
@permission_required('relationship_app.can_add_book')
def add_book(request):
    ...
    # if request.method == 'POST':
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('list_books')
    # else:
    #     form = BookForm()
    # return render(request, 'relationship_app/add_book.html', {'form': form})

@login_required
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    ...
    # book = Book.objects.get(pk=pk)
    # if request.method == 'POST':
    #     form = BookForm(request.POST, instance=book)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('list_books')
    # else:
    #     form = BookForm(instance=book)
    # return render(request, 'relationship_app/edit_book.html', {'form': form})

@login_required
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):   
    ...


from django.http import HttpResponse
def home_view(request):
    return HttpResponse("Welcome to the homepage!")















