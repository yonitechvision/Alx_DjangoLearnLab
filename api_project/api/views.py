from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_queryset(self):
        return Book.objects.all()



from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    ...

from rest_framework import generics
from .models import Book  # Import your model
from .serializers import BookSerializer  # Import your serializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Queryset to retrieve all books
    serializer_class = BookSerializer  # Serializer to convert model instances to JSON


