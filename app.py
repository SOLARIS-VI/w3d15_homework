from flask import Flask, render_template, redirect, request
from models.books import Books
from models.book import Book

app = Flask(__name__)
books = Books()

@app.route('/')
def index():
    return render_template('index.html', library=books.library)

@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']

    book = Book(title, author, genre)
    books.add_book(book)

    return redirect('/')

@app.route('/books/delete/<int:index>', methods=['POST'])
def delete_book(index):
    books.remove_book(index-1)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
