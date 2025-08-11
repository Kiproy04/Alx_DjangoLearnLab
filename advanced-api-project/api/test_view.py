from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.client.login(username="testuser", password="pass1234")

        # Sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_year=2023
        )

        self.list_url = reverse("book-list")   # DRF router name (change if yours is different)
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.pk})

    def test_create_book(self):
        data = {"title": "New Book", "author": "Jane Doe", "publication_year": 2024}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(pk=response.data["id"]).title, "New Book")

    def test_get_books_list(self):
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_update_book(self):
        data = {"title": "Updated Book", "author": "John Doe", "publication_year": 2023}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_url}?author=John Doe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == "John Doe" for book in response.data))

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Test" in book["title"] for book in response.data))

    def test_order_books_by_title(self):
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_permission_denied_for_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
