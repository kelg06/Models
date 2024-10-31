from django.test import TestCase
from app import models


class TestLibrary(TestCase):
    def test_can_checkout_book(self):
        book = models.checkout_book(
            "Janet's Day Out",
            "Markel Gladney",
            True,
            True,
        )

        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Janet's Day Out")
        self.assertEqual(book.author, "Markel Gladney")
        self.assertTrue(book.is_checked_out)
        self.assertTrue(book.is_favorite)

    def test_can_all_books(self):
        books_data = [
            {
                "title": "Ellen's Coming Home",
                "author": "Chris Skeen",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "KSI'S RETURN",
                "author": "Kilan Miller",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "Karate Kids Back in Town",
                "author": "Jacob Allen",
                "is_checked_out": True,
                "is_favorite": True,
            },
        ]

        for book_data in books_data:
            models.checkout_book(
                book_data["title"],
                book_data["author"],
                book_data["is_checked_out"],
                book_data["is_favorite"],
            )

        books = models.all_books()

        self.assertEqual(len(books), len(books_data))

        books_data = sorted(books_data, key=lambda c: c["title"])
        books = sorted(books, key=lambda c: c.title)

        for data, book in zip(books_data, books):
            self.assertEqual(data["title"], book.title)
            self.assertEqual(data["author"], book.author)
            self.assertEqual(data["is_checked_out"], book.is_checked_out)
            self.assertEqual(data["is_favorite"], book.is_favorite)

    def test_can_find_book_by_title(self):
        books_data = [
            {
                "title": "Ellen's Coming Home",
                "author": "Chris Skeen",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "KSI'S RETURN",
                "author": "Kilan Miller",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "Karate Kids Back in Town",
                "author": "Jacob Allen",
                "is_checked_out": True,
                "is_favorite": True,
            },
        ]

        for book_data in books_data:
            models.checkout_book(
                book_data["title"],
                book_data["author"],
                book_data["is_checked_out"],
                book_data["is_favorite"],
            )

        self.assertIsNone(models.find_book_by_title("aousnth"))

        book = models.find_book_by_title("Ellen's Coming Home")

        self.assertIsNotNone(book)
        self.assertEqual(book.author, "Chris Skeen")

    def test_can_favorite_book(self):
        books_data = [
            {
                "title": "Ellen's Coming Home",
                "author": "Chris Skeen",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "KSI'S RETURN",
                "author": "Kilan Miller",
                "is_checked_out": True,
                "is_favorite": False,
            },
            {
                "title": "Karate Kids Back in Town",
                "author": "Jacob Allen",
                "is_checked_out": True,
                "is_favorite": True,
            },
        ]

        for book_data in books_data:
            models.checkout_book(
                book_data["title"],
                book_data["author"],
                book_data["is_checked_out"],
                book_data["is_favorite"],
            )

        self.assertEqual(len(models.favorite_book()), 3)

    def test_can_update_book_author(self):
        books_data = [
            {
                "title": "Ellen's Coming Home",
                "author": "Chris Skeen",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "KSI'S RETURN",
                "author": "Kilan Miller",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "Karate Kids Back in Town",
                "author": "Jacob Allen",
                "is_checked_out": True,
                "is_favorite": True,
            },
        ]

        for book_data in books_data:
            models.checkout_book(
                book_data["title"],
                book_data["author"],
                book_data["is_checked_out"],
                book_data["is_favorite"],
            )

        models.update_book_author("Chris Skeen", "Robbin Skeen")

        self.assertEqual(
            models.find_book_by_title("Ellen's Coming Home").title, "Ellen's Coming Home"
        )

    def test_can_delete_book(self):
        books_data = [
            {
                "title": "Ellen's Coming Home",
                "author": "Chris Skeen",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "KSI'S RETURN",
                "author": "Kilan Miller",
                "is_checked_out": True,
                "is_favorite": True,
            },
            {
                "title": "Karate Kids Back in Town",
                "author": "Jacob Allen",
                "is_checked_out": True,
                "is_favorite": True,
            },
        ]

        for book_data in books_data:
            models.checkout_book(
                book_data["title"],
                book_data["author"],
                book_data["is_checked_out"],
                book_data["is_favorite"],
            )

        models.delete_book("Ellen's Coming Home")

        self.assertEqual(len(models.all_books()), 2)
