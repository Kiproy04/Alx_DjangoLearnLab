from django.contrib import admin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')
    search_fields = ('username', 'email')

# Register your models here.
admin.ModelAdmin
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)