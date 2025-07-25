from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register
urlpatterns = [ 
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', views.UserCreationForm.as_view(), name='admin_detail'),
    path('librarian/', views.UserCreationForm.as_view(template_name='librarian_view.html'), name='librarian_detail'),
    path('member/', views.UserCreationForm.as_view(), name='member_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]