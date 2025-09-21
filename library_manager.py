"""
library_manager.py

Main module for library management of Book objects.

Provides:
- Functions to add books, list all books, and find books.
- Command-line interface for user interaction.
"""
from book import Book

def add_book(library):
    """
    Prompts user to input book details and adds a new Book object to the library.

    Args:
        library (list): The list of Book objects in the library

    Returns:
        None
    """
    title = input("Enter in the title of the book: ")
    author = input("Enter in the author of the book: ")
    isbn = input("Enter in the ISBN of the book: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)
    print(f"Book '{title}' by {author} successfully added to the library.")


def list_books(library):
    """
    This function prints the details of all books in the library.

    Args:
        library (list): The list of book objects in the library system.

    Returns:
        None
    """
    if not library:
        print("There are currently no books in the library.")
        return
    
    print("\nLibrary Catalog:")
    for book in library:
        print(f"- Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")


def find_book(library, query):
    """
    This function searches for a book with matching title or author.

    Args:
        library (list): The list of Book objects to search
        query (str): The title or author to search for (case-insensitive.)

    Returns:
        Book: Returns the first Book object that matches the query by title or author.
        None: Returns None if no match is found.
    """
    query = query.lower()

    # Note: 'in' here instead of '==' would accept partial matches instead of exact
    # if query in book.title.lower() or query in book.author.lower():
    for book in library:
        if book.title.lower() == query or book.author.lower() == query:
            return book
    return None


def main():
    """
    Presents a menu to user with options using a while loop.

    Functions:
        1. Add a new book
        2. List all books
        3. Find a book by title or author
        4. Exit the program
    """
    my_library = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "9783257691078"),
    Book("The Hunger Games", "Suzanne Collins", "9780545229937"),
    Book("High Fidelity", "Nick Hornsby", "9781573225519"),
    Book("The Boxcar Children", "Gertrude Chandler Warner", "9780593898239")
    ]

    while True:
        print("Library Menu Options:")
        print("1. Add a new book.")
        print("2. List all books.")
        print("3. Find a book.")
        print("4. Exit the program.")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_book(my_library)
        elif choice == "2":
            list_books(my_library)
        elif choice == "3":
            query = input("Enter title or author to search: ")
            result = find_book(my_library, query)
            if result:
                print(f"Book found: {result}")
            else:
                print(f"No book found matching '{query}'.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print(f"Invalid option '{choice}'. Try again.")


if __name__ == "__main__":
    main()
