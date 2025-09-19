"""
book.py
"""
class Book:
    """A class to store all book objects in the system."""

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