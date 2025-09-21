"""
book.py

Module to define Book class to represent books in a library.

Implements methods to initialize book objects, fetch details,
and returns formatted string representation.
"""
class Book:
    """
    A class to store all book objects in the system.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book.
    """

    def __init__(self, title, author, isbn):
        """
        Initializes a Book object and attributes.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN number of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        """
        Method returns a formatted string of the Book.

        Returns:
            str: Formatted string including title, author, and ISBN.
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    def get_details(self):
        """
        Method returns book details as a dictionary.

        Returns:
            dict: A dictionary containing the book's 'title', 'author', and 'isbn'.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }


if __name__ == "__main__":
    # Prints test example to demonstrate Book object and __str__ method
    test_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9783257691078")
    print(test_book)
    