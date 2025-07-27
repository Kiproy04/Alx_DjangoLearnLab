from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class CustomUser(AbstractUser):
        date_of_birth = models.DateField()
        profile_photo = models.ImageField()

class CustomUserManager(BaseUserManager):
        def create_user(self, username, email, password=None, **extra_fields):
                if not email:
                        raise ValueError('The Email field must be set')
                email = self.normalize_email(email)
                user = self.model(username=username, email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user

        def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None):
                user = self.create_user(
                email,
                password=password,
                date_of_birth=date_of_birth,
                profile_photo=profile_photo,
                username=username,
                )

                user.is_admin = True
                user.save(using=self._db)
                return user
        
class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=100)
        publication_year = models.IntegerField()

        def __str__(self):
                return f"Book: {self.title} {self.author} {self.publication_year}"
        
        class Meta:
                permissions = [
                        ("can_view_book", "Can view book"),  
                        ("can_create_book", "Can create book"),
                        ("can_edit_book", "Can edit book" ),
                        ("can_delete_book", "Can delete book"),
                ]