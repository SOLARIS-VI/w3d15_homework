from flask import render_template, request, redirect
from app import app
from models.books import Books
from models.book import Book

books = Books()

@app.route('/')
def index():
    return render_template('index.html', library=books.library)

# show book
@app.route('/books/<int:index>')
def show_book(index):
    book = books.library[index]
    return render_template('book_detail.html', book=book, index=index)

# add book
@app.route('/books/new', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        book = Book(title=title, author=author, genre=genre)
        books.add_book(book)
        return redirect('/')
    return render_template('new_book.html')

# delete book
@app.route('/books/<int:index>/delete', methods=['POST'])
def delete_book(index):
    book = books.library[index]
    books.remove_book(book)
    return redirect('/')
