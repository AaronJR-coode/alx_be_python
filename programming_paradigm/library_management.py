
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return f"'{self.title}' is already checked out."
        self._is_checked_out = True
        return f"'{self.title}' has been checked out."

    def return_book(self):
        if not self._is_checked_out:
            return f"'{self.title}' wasn't checked out."
        self._is_checked_out = False
        return f"'{self.title}' has been returned."

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        return f"'{book.title}' added to the library."

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.check_out()
        return f"Book titled '{title}' not found."

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"Book titled '{title}' not found."

    def list_available_books(self):
        available_books = [str(book) for book in self._books if not book._is_checked_out]
        if available_books:
            return "\n".join(available_books)
        return "No books are currently available."