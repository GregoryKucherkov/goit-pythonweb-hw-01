from abc import ABC, abstractmethod

class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

class LibraryInterface(ABC):

    @abstractmethod
    def add_book(self, book: Book):
        pass
    
    @abstractmethod
    def remove_book(self, title: str):
        pass
    
    @abstractmethod
    def show_books(self):
        pass

    @abstractmethod
    def get_books(self) -> list:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book {title} not found")

    def show_books(self):
        if self.books:
            for book in self.books:
                print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')
        else:
            print("No books in library")

    def get_books(self) -> list:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f"Book '{title}' by {author} added to the library.")

    def remove_book(self, title: str):
        self.library.remove_book(title)
 

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

   

    

