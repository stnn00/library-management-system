"""
library_manager.py
"""

from book import Book

def add_book(library):
    """
    Prompts user to input book details and adds a new Book object to the library.

    Parameters:
    library (list): List of Book objects in the library
    """
    title = input("Enter in the title of the book: ")
    author = input("Enter in the author of the book: ")
    isbn = input("Enter in the ISBN of the book: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)