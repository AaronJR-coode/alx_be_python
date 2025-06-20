class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.author}"

    def __repr__(self):
        print(f"Book: {self.title}, {self.author}")
    
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} EBook, {self.file_size} MB"
    
    def __repr__(self):
        print(f"EBook: {self.title}, {self.author}, {self.file_size}")
    
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} print, {self.page_count} pages"
    
    def __repr__(self):
        print(f"PrintBook: {self.title}, {self.author}, {self.page_count}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Only Book (or subclasses) can be added")
        self.books.append(book)
        return f"Created: {book}"


    def list_books(self):
        if not self.books:
            return "Library is empty."
        for idx, book in enumerate(self.books):
            print(f"{book}") 

