from django.contrib import admin
from .models import Book, UserProfile, Author, Library, Librarian

# Register your models here.
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
