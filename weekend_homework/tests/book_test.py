import unittest

from models import book_list
from models.book import Book

class TestBook(unittest.TestCase):

    def test_book_has_title(self):
        self.assertEqual("Naked Lunch", book_list.book1.title)
    
    def test_show_library(self):
        self.assertEqual(book_list.books, book_list.show_library(book_list.books))

    def test_show_book(self):
         self.assertEqual(book_list.book1, book_list.show_book(book_list.book1))

    def test_add_book(self):
        book_list.books = []
        book4 = Book("The Rise of Red Clydeside", "Kenny MacAskill", "history", True)
        book_list.add_book(book4)
        self.assertEqual(1, len(book_list.books))

    def test_remove_book(self):
        book_list.books = [book_list.book1]
        book_to_remove = Book("Naked Lunch", "William Borroughs", "science fiction", True)
        book_list.add_book(book_to_remove)
        book_list.remove_book(book_to_remove)
        self.assertEqual(1, len(book_list.books))
    
    