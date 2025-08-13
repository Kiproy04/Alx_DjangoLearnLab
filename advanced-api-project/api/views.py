from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend 
from django_filters import rest_framework 

# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

     # Adding filter, search, ordering backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields (exact match)
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching fields (partial match, case-insensitive)
    search_fields = ['title', 'author']

    # Ordering fields (asc/desc via ?ordering=)
    ordering_fields = ['title', 'publication_year', 'created_at']

    # Default ordering if none provided
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # attach the current user to created_by automatically
        serializer.save(created_by=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # if you need to do something special when updating, override perform_update
    def perform_update(self, serializer):
        serializer.save() 

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, serializer):
        serializer.delete()



