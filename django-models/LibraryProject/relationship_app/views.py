from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Author, Librarian, UserProfile
from .models import Library
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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

# class UserCreationForm():
#     form_class = UserCreationForm
#     success_url = '/login/'
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(self.success_url)
#         return render(request, self.template_name, {'form': form})
# from django.contrib.auth import views as auth_views
# class LoginView(auth_views.LoginView):
#     template_name = 'relationship_app/login.html'
# class LogoutView(auth_views.LogoutView):
#     template_name = 'relationship_app/logout.html'


#     # template_name = 'relationship_app/register.html'

# def is_admin(user):
#     return hasattr(user, 'UserProfile') and user.UserProfile.role == 'Admin'

# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# def is_member(user):
#     return hasattr(user, 'UserProfile') and user.UserProfile.role == 'Member'

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')
    
# def is_librarian(user):
#     return hasattr(user, 'UserProfile') and user.UserProfile.role == 'Librarian'

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')
# @login_required    
# class Register:
#     def register_view(request):
#         if request.method == 'POST':
#             form = UserCreationForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login(request, user)
#                 return redirect('home')
#         else:
#             form = UserCreationForm()
#         return render(request, 'relationship_app/register.html', {'form': form})

# @permission_required
# relationship_app.can_add_book 
# relationship_app.can_change_book
# relationship_app.can_delete_book
















