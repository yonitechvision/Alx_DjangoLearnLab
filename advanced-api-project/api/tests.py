from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(title="Book 1", publication_year=2020, author=self.author)

    def test_book_list(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_detail(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {"title": "New Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
