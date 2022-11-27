from models.book import Book

book1 = Book("Naked Lunch", "William Borroughs", "science fiction", True)
book2 = Book("Northern Lights: The Golden Compass", "Phillip Pullman", "fantasy", False)
book3 = Book("No Mean City", "Herbert Kingsley Long", "thriller", True)

books = [book1, book2, book3]

def show_library(books):
    return books

def show_book(book):
    return book

def add_book(book):
    books.append(book)

def remove_book(book_to_remove):
    book_to_remove = None
    for book in books:
        if book.title == book.title:
            book_to_remove = book
            break

    books.remove(book_to_remove)





