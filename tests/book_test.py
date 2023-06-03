# import unittest
# from models.book import Book

# class TestBook(unittest.TestCase):
#     def test_book_properties1(self):
#         book = Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy")
#         self.assertEqual(book.title, "The Lord of the Rings")
#         self.assertEqual(book.author, "J.R.R. Tolkien")
#         self.assertEqual(book.genre, "Fantasy")

#     def test_book_properties2(self):
#         book = Book("Foundation", "Issac Asimov", "Science Fiction")
#         self.assertEqual(book.title, "Foundation")
#         self.assertEqual(book.author, "Issac Asimov")
#         self.assertEqual(book.genre, "Science Fiction")

#     def test_book_properties3(self):
#         book = Book("A Brief History of Time", "Stephen Hawking", "Non Fiction")
#         self.assertEqual(book.title, "A Brief History of Time")
#         self.assertEqual(book.author, "Stephen Hawking")
#         self.assertEqual(book.genre, "Non Fiction")

import unittest
from models.book import Book

book1 = Book("The Lord of The Rings", "J.R.R Tolkien", "Fantasy", False)
book2 = Book("Foundation", "Isaac Asimov", "Science Fiction", False)
book3 = Book("A Brief History of Everything", "Stephen Hawking", "Non Fiction", True)

book_list = [book1, book2, book3]

def add_new_book(new_book):
    book_list.append(new_book)

def delete_book(index):
    book_list.pop(index)

def check_out(selected_book_index):
    if book_list[selected_book_index].checked_out == False:
        book_list[selected_book_index].checked_out = True
    if book_list[selected_book_index].checked_out == True:
        book_list[selected_book_index].checked_out = False

if __name__ == '__main__':
    unittest.main()
