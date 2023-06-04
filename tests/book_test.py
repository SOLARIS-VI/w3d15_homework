import unittest
from models.book import Book
from models.books import Books

class TestBook(unittest.TestCase):
    def setUp(self):
        self.books = Books()
        self.book1 = Book("The Lord of The Rings: The Fellowship of The Ring", "J.R.R Tolkien", "Fantasy")
        self.book2 = Book("Foundation", "Isaac Asimov", "Science Fiction")
        self.book3 = Book("A Brief History of Everything", "Stephen Hawking", "Non Fiction")
        self.book4 = Book("1984", "George Orwell", "Dystopian Fiction")
        self.book5 = Book("To Kill a Mockingbird", "Harper Lee", "Classic")
        self.book6 = Book("Pride and Prejudice", "Jane Austen", "Classic")
        self.book7 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
        self.book8 = Book("The Catcher in the Rye", "J.D. Salinger", "Classic")
        self.book9 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
        self.book10 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy")
        self.book11 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction")
        self.book12 = Book("The Da Vinci Code", "Dan Brown", "Thriller")
        
        self.books.add_book(self.book1)
        self.books.add_book(self.book2)
        self.books.add_book(self.book3)
        self.books.add_book(self.book4)
        self.books.add_book(self.book5)
        self.books.add_book(self.book6)
        self.books.add_book(self.book7)
        self.books.add_book(self.book8)
        self.books.add_book(self.book9)
        self.books.add_book(self.book10)
        self.books.add_book(self.book11)
        self.books.add_book(self.book12)

    def test_remove_book(self):
        self.books.remove_book(1)
        self.assertEqual(len(self.books.library), 11)
        self.assertEqual(self.books.library[0].title, "The Lord of The Rings: The Fellowship of The Ring")
        self.assertEqual(self.books.library[1].title, "A Brief History of Everything")
        self.assertEqual(self.books.library[2].title, "1984")
        self.assertEqual(self.books.library[3].title, "To Kill a Mockingbird")
        self.assertEqual(self.books.library[4].title, "Pride and Prejudice")
        self.assertEqual(self.books.library[5].title, "The Great Gatsby")
        self.assertEqual(self.books.library[6].title, "The Catcher in the Rye")
        self.assertEqual(self.books.library[7].title, "The Hobbit")
        self.assertEqual(self.books.library[8].title, "Harry Potter and the Sorcerer's Stone")
        self.assertEqual(self.books.library[9].title, "The Hitchhiker's Guide to the Galaxy")
        self.assertEqual(self.books.library[10].title, "The Da Vinci Code")

if __name__ == '__main__':
    unittest.main()
