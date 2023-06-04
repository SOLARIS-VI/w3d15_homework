from flask import render_template, request, redirect
from app import app
from models.books import Books
from models.book import Book

books = Books()

@app.route('/')
def index():
    return render_template('index.html', books=books.library)

@app.route('/books/<int:index>')
def show_book(index):
    book = books.library[index]
    return render_template('book_detail.html', book=book, index=index)

@app.route('/books/new', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        book = Book(title, author, genre, False)  # Set checked_out to False by default
        books.add_book(book)
        return redirect('/')
    return render_template('new_book.html')

@app.route('/books/<int:index>/delete', methods=['POST'])
def delete_book(index):
    books.remove_book(index)
    return redirect('/')

