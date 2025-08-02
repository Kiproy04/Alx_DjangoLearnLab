from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register, member_view, admin_view, librarian_view
urlpatterns = [ 
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', views.admin_view, name='admin_detail'),
    path('librarian/', views.librarian_view, name='librarian_detail'),
    path('member/', views.member_view, name='member_detail'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('add_book/', views.add_book, name='add'),
    path('edit_book/', views.edit_book, name='edit'),
    path('delete_book/', views.delete_book, name='delete'),
    path('', views.home_view, name='home'),
]