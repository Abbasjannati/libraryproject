from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
def home(request):
    search = request.GET.get('search', '')

    if search:
        books = Book.objects.filter(title__icontains=search)
    else:
        books = Book.objects.all()
    context = {
        'name': 'Abbas zaidi',
        'books': books
        

    }
    return render(request, 'home.html',context)

# API view to get all books
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# Create your views here.
