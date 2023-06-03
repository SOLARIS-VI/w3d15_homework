class Books:
    def __init__(self):
        self.library = []

    def add_book(self, book):
        self.library.append(book)

    def remove_book(self, book):
        self.library.remove(book)
