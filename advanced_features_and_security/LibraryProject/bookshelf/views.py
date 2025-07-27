from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('bookshelf.can_view_book', raise_exception=True)
def view_books(request):
   ...

