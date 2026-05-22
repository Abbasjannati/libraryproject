from django.shortcuts import render

from .models import Book

def home(request):
    books = Book.objects.all()
    context = {
        'name': 'Abbas zaidi',
        'books': books
        

    }
    return render(request, 'home.html',context)


# Create your views here.
