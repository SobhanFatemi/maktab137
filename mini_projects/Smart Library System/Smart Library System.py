import pickle
from datetime import datetime, timedelta

LIBRARY_PATH = "library_data.pkl"

def save_library(library):
    with open(LIBRARY_PATH, "wb") as f:
        pickle.dump(library, f)
    print("Library data saved successfully.")

def load_library():
    try:
        with open(LIBRARY_PATH, "rb") as file:
            library = pickle.load(file)
        print("Library data loaded successfully.")
        return library
    except FileNotFoundError:
        print("No previous data found, creating new library.")
        return Library([], [])

class Member():
    def __init__(self, name, id, email, borrowed_books):
        self.name = name
        self.id = id
        self.email = email
        self.borrowed_books = borrowed_books

    def borrow_book(self):
        raise NotImplementedError("Subclasses must implement this method!")

    def return_book(self, book):
        if book in self.borrowed_books:
            returned = datetime.now()
            time_difference = book.return_date - returned

            if time_difference.total_seconds() > 0:
                print(f"You returned the book early by {time_difference}.")
            elif time_difference.total_seconds() < 0:
                print(f"You returned the book late by {-time_difference}.")
            else:
                print("You returned the book exactly on time!")

            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"'{self.name}' returned: '{book.title}'!")
        else:
            print(f"'{self.name}' has not borrowed: '{book.title}'!")

    def show_info(self):
        print(f"\nName: '{self.name}'\nMember ID: '{self.id}'\nEmail: '{self.email}'")
        print("Borrowed books: ")
        if self.borrowed_books:
            for i, book in enumerate(self.borrowed_books):
                print(f"#{i+1}: '{book}'")
        else:
            print(f"Has not borrowed any books yet!")
              

class Book:
    total_books = 0
    
    def __init__(self, title, author, isbn, is_borrowed=False, borrowed_date=None, return_date=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        Book.total_books += 1

        def __str__():
            return f"Total books created: {Book.total_books}"

    def mark_as_borrowed(self):
        self.is_borrowed = True
        self.borrowed_date = datetime.now()
        self.return_date = self.borrowed_date + timedelta(weeks=1)

    def mark_as_returned(self):
        self.borrowed_date = None
        self.return_date = None
        self.is_borrowed = False

    def display_info(self):
        print(f"\nTitle: '{self.title}'\nAuthor: '{self.author}'\nISBN: '{self.isbn}'\nIs borrowed: '{self.is_borrowed}'")


class Library:
    def __init__(self, books, members):
        self.books = books
        self.members = members

    def add_book(self, *books):
        for book in books:
            if book not in self.books:
                self.books.append(book)
                print(f"'{book.title}' was added to the library.")
            else:
                print(f"'{book.title}' is already in the library!")

    def add_member(self, *members):
        for member in members:
            if member not in self.members:
                self.members.append(member)
                print(f"'{member.name}' was added as a member to the library.")
            else:
                print(f"'{member.name}' is already a member in the library!")

    def books_status(self):
        available = 0
        for book in self.books:
            if not book.is_borrowed:
                available += 1
        unavailable = len(self.books) - available
        print(f"Available books: {available}\nBorrowed books: {unavailable}")

    def borrow_book(self, member_id, isbn):
        member_found = False
        book_found = False
        for member in self.members:
            if member_id == member.id:
                member_found = True
                for book in self.books:
                    if isbn == book.isbn:
                        book_found = True
                        member.borrow_book(book)
        if not member_found:
            print("Member Not found!")
        elif not book_found:
            print("Book Not found!")

    def return_book(self, member_id, isbn):
        member_found = False
        book_found = False
        for member in self.members:
            if member_id == member.id:
                member_found = True
                for book in self.books:
                    if isbn == book.isbn:
                        book_found = True
                        member.return_book(book)
        if not member_found:
            print("Member Not found!")
        elif not book_found:
            print("Book Not found!")

    def search_book_by_title(self, title):
        found = False
        for book in self.books:
            if book.title == title:
                found = True
                book.display_info()
        if not found:
            print("Book not found!")

    def search_member_by_name(self, name):
        found = False
        for member in self.members:
            if member.name == name:
                found = True
                member.show_info()
        if not found:
            print("Member not found!")
    
    def show_all_books(self):
        for i, book in enumerate(self.books):
            print(f"#{i+1}: '{book.title}'")
    
    def show_all_members(self):
        for i, member in enumerate(self.members):
            print(f"#{i+1}: '{member.name}'")

class StudentMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:
            if self in library.members:
                if book in library.books:
                    if book not in self.borrowed_books:
                        if book.is_borrowed:
                            print(f"'{book.title}' is already borrowed!")
                        else:
                            book.mark_as_borrowed()
                            self.borrowed_books.append(book)
                            print(f"'{self.name}' borrowed: '{book.title}'!\nReturn date: '{book.return_date}")
                    else:
                        print(f"'{self.name}' has already borrowed: '{book.title}'!")
                else:
                    print("This book is not in the library!")
            else:
                print(f"'{self.name}' is not a member!")
        else:
            print(f"'{self.name}' already has borrowed 3 books!")

class TeacherMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 5:
            if self in library.members:
                if book in library.books:
                    if book not in self.borrowed_books:
                        if book.is_borrowed:
                            print(f"'{book.title}' is already borrowed!")
                        else:
                            book.mark_as_borrowed()
                            self.borrowed_books.append(book)
                            print(f"'{self.name}' borrowed: '{book.title}'!\nReturn date: '{book.return_date}")
                    else:
                        print(f"'{self.name}' has already borrowed: '{book.title}'!")
                else:
                    print("This book is not in the library!")
            else:
                print(f"'{self.name}' is not a member!")
        else:
            print(f"'{self.name}' already has borrowed 5 books!")
        
    
library = load_library()