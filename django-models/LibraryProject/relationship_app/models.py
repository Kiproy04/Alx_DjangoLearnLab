from django.db import models
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(Admin, Librarian, Member)
class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

@permission_required
class Book(models.Model):
    class Meta:
        permissions = [
            "relationship_app.can_add_book", 
            "relationship_app.can_change_book", 
            "relationship_app.can_delete_book",
        ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.title} {self.author}"
    
    

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"Library: {self.name} {self.books}"

class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian: {self.name} {self.library}"