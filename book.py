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
    
    def __str__(self):
        """Method returns a formatted string of the Book."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    def get_details(self):
        """
        Method returns book details as a dictionary.

        Returns:
            dict: A dictionary containing keys 'title', 'author', and 'isbn'.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }


if __name__ == "__main__":
    # Prints test result for Book object
    test_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9783257691078")
    print(test_book)