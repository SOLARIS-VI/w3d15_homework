import unittest
from models.book import Book
from models.books import Books

class TestBook(unittest.TestCase):
    def setUp(self):
        self.books = Books()
        self.book1 = Book("The Lord of The Rings", "J.R.R Tolkien", "Fantasy")
        self.book2 = Book("Foundation", "Isaac Asimov", "Science Fiction")
        self.book3 = Book("A Brief History of Everything", "Stephen Hawking", "Non Fiction")
        self.books.add_book(self.book1)
        self.books.add_book(self.book2)
        self.books.add_book(self.book3)

    def test_remove_book(self):
        self.books.remove_book(1)
        self.assertEqual(len(self.books.library), 2)
        self.assertEqual(self.books.library[0].title, "The Lord of The Rings")
        self.assertEqual(self.books.library[1].title, "A Brief History of Everything")

if __name__ == '__main__':
    unittest.main()
