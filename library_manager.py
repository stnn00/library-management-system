"""
library_manager.py

Module with functions for library management of Book objects:
- add_book: add a new book from user input
- list_books: displays all books in library
- find_book: search for a book with matching title or author
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

def list_books(library):
    """
    This function prints the details of all books in the library.
    """
    if not library:
        print("There are currently no books in the library.")
        return
    
    print("\nLibrary Catalog:")
    for book in library:
        print(book)

def find_book(library, query):
    """
    This function searches for a book with matching title or author.
    """
    query = query.lower()
    for book in library:
        if book.title.lower() == query or book.author.lower() == query:
            return book
    return None

if __name__ == "__main__":
    library = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", 9783257691078),
        Book("The Hunger Games", "Suzanne Collins", 9780545229937)
    ]

    add_book(library)

    list_books(library)

    result = find_book(library, "I Am Number Four")
    print(result)

    result = find_book(library, "The Great Gatsby")
    print(result)
    
    result = find_book(library, "the great gatsby")
    print(result)

    result = find_book(library, "Suzanne collins")
    print(result)