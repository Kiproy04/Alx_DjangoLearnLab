from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .form import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
   ...

