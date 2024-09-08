from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.id})
def test_create_book(self):
    url = reverse('book-list')
    data = {
        "title": "New Book",
        "publication_year": 2024,
        "author": self.author.id
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 2)
    self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")
def test_get_book(self):
    response = self.client.get(self.book_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], "Harry Potter")

def test_update_book(self):
    data = {
        "title": "Harry Potter and the Philosopher's Stone",
        "publication_year": 1997,
        "author": self.author.id
    }
    response = self.client.put(self.book_url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    self.assertEqual(Book.objects.get(id=self.book.id).title, "Harry Potter and the Philosopher's Stone")
def test_delete_book(self):
    response = self.client.delete(self.book_url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 0)

def test_filter_books_by_author(self):
    url = reverse('book-list') + '?author__name=J.K.%20Rowling'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['author']['name'], "J.K. Rowling")

def test_search_books(self):
    url = reverse('book-list') + '?search=Harry'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], "Harry Potter")

def test_order_books_by_publication_year(self):
    url = reverse('book-list') + '?ordering=-publication_year'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['title'], "Harry Potter")


