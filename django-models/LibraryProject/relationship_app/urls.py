from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
urlpatterns = [ 
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', views.AdminDetailView.as_view(), name='admin_detail'),
    path('librarian/', views.LibrarianDetailView.as_view(), name='librarian_detail'),
    path('member/', views.MemberDetailView.as_view(), name='member_detail'),
]