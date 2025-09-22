# library-management-system

A simple, modular Python program to manage a library's book inventory.

## Overview

This program offers a menu-driven interface to manage a library. Users can add new books, view the library catalog, or search for books by title or author.

This project is composed of two Python modules:

- `book.py` – Defines the `Book` class, representing books as objects with attributes `title`, `author`, and `isbn`.
- `library_manager.py` – Provides functionality to add, list, and search books through a command-line menu.

Users can interact with a pre-defined sample library to test and explore the program.

## Demonstration

Video on YouTube to demonstrate and explain Python modules (4:02)

- **[https://youtu.be/W6O8A-IJmDY](https://youtu.be/W6O8A-IJmDY)**

## Features

- Add new books to the library by providing title, author, and ISBN.
- View a complete list of books in the library.
- Search for books by title or author.
- User-friendly command-line interface with menu options.
- Sample library included for demonstration purposes.

## Installation & Usage

Instructions to set up and run the Library Management System:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/stnn00/library-management-system.git
   cd library-management-system

2. **Run the program**

   Start library management system by running:

   ```bash
   python library_manager.py

3. **Using the program**

   After running the program, a menu will appear:

   ```text
   Library Menu Options:
   1. Add a new book.
   2. List all books.
   3. Find a book.
   4. Exit the program.
4. **Type the number corresponding to your choice and press Enter.**
   - Add a new book: Choose option `1` and enter the book's title, author, and ISBN.
   - View entire library catalog: Choose option `2` to display all books.
   - Find a book: Choose option `3` and enter a title or author to search.
   - Exit the program: Choose option `4` to close the application.</br>
</br>

*Tip: Any added books will only be temporarily stored for the current session.*