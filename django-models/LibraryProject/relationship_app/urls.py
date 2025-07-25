from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register
urlpatterns = [ 
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', views.admin_view(template_name='admin_view.html'), name='admin_detail'),
    path('librarian/', views.librarian_view(template_name='librarian_view.html'), name='librarian_detail'),
    path('member/', views.member_view(template_name='member_view.html'), name='member_detail'),
    path('login/', LoginView(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('add_book/', views.add_book, name='add'),
    path('edit_book/', views.edit_book, name='edit'),
    path('delete_book/', views.delete_book, name='delete'),
]