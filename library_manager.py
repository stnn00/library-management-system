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
    for book in library:
        if book.title == query or book.author == query:
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