
class Book:
    def __init__(self, title, author, isbn, is_checked_out =False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def check_out(self):
        self.is_checked_out = True
        return(f'The book is {self.is_checked_out}')

    def return_book(self):
        self.is_checked_out = False
        return(f'The book is not checked out {self.is_checked_out}')

    def __str__(self):
        return(f'The books title is {self.title}\n The author is {self.author}\n The isbn is {self.isbn}')

book1 = Book('The Pelican Brief', 'John Grisham', 'y6734')
book2 = Book('A time to kill', 'John Grisham', 'rt9087')

book1.return_book()
#print(book1)

book2.__str__()
book2.check_out()

class Library():
    def __innit__(self, books=[]):
        self.books = books

    def add_book(self, book):
        self.book = book
        return self.books.append(book)
    
    def remove_book(self, isbn):
        self.isbn = isbn
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return
        print('Error: Book not found')
   
    def check_out_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_checked_out():
                    print('Error:Book already checked out.')
                else:
                    book.check_out()
                    print('Book checked out successfully.')
                    return
        print('Error: Book not found')

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_checked_out:
                    book.return_book()
                    print('Book returned scuccessfully')
                else:
                    print('Error:Book is not checked out.')
                return
        print('Error: Book not found.')
            

# Example usage:

# Create some books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

# Create a library
library = Library()

# Add books to the library
print(library.add_book(book1))
print(library.add_book(book2))

# List all books in the library
print(library.list_books())

# Check out a book
print(library.check_out_book("9780316769488"))

# List all books in the library after checking out
print(library.list_books())

# Return a book
print(library.return_book("9780316769488"))

# List all books in the library after returning
print(library.list_books())





   