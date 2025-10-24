import pickle
import os
from datetime import datetime, timedelta
from abc import ABC, abstractmethod


LIBRARY_PATH = "library_data.pkl"

def save_library(library, user_path=None):
    while True:
        if not user_path:
            user_path = input("Enter the file path to save the library: ").strip()
        if not user_path:
            print("File path cannot be empty!")
            continue

        if os.path.exists(user_path) and user_path != LIBRARY_PATH:
            overwrite = input(f"'{user_path}' already exists. Replace it? (y/n): ").strip().lower()
            if overwrite == 'y':
                try:
                    with open(user_path, "wb") as file:
                        pickle.dump(library, file)
                    print(f"Library saved successfully to '{user_path}'!")
                    break
                except Exception as e:
                    print(f"Error saving library: {e}")
                    break
            elif overwrite == 'n':
                try_again = input("Do you want to choose a different file path? (y/n): ").strip().lower()
                if try_again == 'y':
                    continue
                else:
                    print("Save canceled!")
                    break
            else:
                print("Invalid input!")
        else:
            try:
                with open(user_path, "wb") as f:
                    pickle.dump(library, f)
                print(f"Library saved successfully to '{user_path}'!")
                break
            except Exception as e:
                print(f"Error saving library: {e}")
                break

def load_library(user_path=None):
    while True:
        if not user_path:
            user_path = input("Enter the file path to load the library: ").strip()
        if not user_path:
            print("Path cannot be empty. Please try again.")
            user_path = None
            continue

        if not os.path.exists(user_path):
            print(f"File '{user_path}' does not exist.")
            choice = input("Do you want to create a new empty library? (y/n): ").strip().lower()
            if choice == 'y':
                print("Creating a new empty library...")
                return Library([], [])
            else:
                print("Please enter another file path!")
                user_path = None
                continue

        try:
            with open(user_path, "rb") as file:
                library = pickle.load(file)
            print(f"Library loaded successfully from '{user_path}'!")
            return library
        
        except Exception as e:
            print(f"An unexpected error occurred while loading: {e}")
            retry = input("Try again? (y/n): ").strip().lower()
            if retry == 'y':
                user_path = None
                continue
            else:
                print("Creating a new empty library...")
                return Library([], [])
                

class Member():
    def __init__(self, name, id, email, borrowed_books):
        self.name = name
        self.id = id
        self.email = email
        self.borrowed_books = borrowed_books


    def borrow_book(self):
        raise NotImplementedError

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
    total_books = []
    
    def __init__(self, title, author, isbn, is_borrowed=False, borrowed_date=None, return_date=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        Book.total_books.append(self)

    def __len__(self):
        return len(self.total_books)

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

    def borrow_book(self, member_id, isbn):
        member_found = False
        book_found = False
        for member in self.members:
            if member_id == member.id:
                member_found = True
                for book in self.books:
                    if isbn == book.isbn:
                        book_found = True
                        member.borrow_book(book, self)
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
    
    def books_status(self):
        available = 0
        for book in self.books:
            if not book.is_borrowed:
                available += 1
        unavailable = len(self.books) - available
        print(f"Available books: {available}\nBorrowed books: {unavailable}")

class StudentMember(Member):
    def borrow_book(self, book, library):
        if len(self.borrowed_books) < 3:
            if self in library.members:
                if book in library.books:
                    if book not in self.borrowed_books:
                        if book.is_borrowed:
                            print(f"'{book.title}' is already borrowed!")
                        else:
                            book.mark_as_borrowed()
                            self.borrowed_books.append(book)
                            print(f"'{self.name}' borrowed: '{book.title}'!\nReturn date: '{book.return_date}'")
                    else:
                        print(f"'{self.name}' has already borrowed: '{book.title}'!")
                else:
                    print("This book is not in the library!")
            else:
                print(f"'{self.name}' is not a member!")
        else:
            print(f"'{self.name}' already has borrowed 3 books!")

class TeacherMember(Member):
    def borrow_book(self, book, library):
        if len(self.borrowed_books) < 5:
            if self in library.members:
                if book in library.books:
                    if book not in self.borrowed_books:
                        if book.is_borrowed:
                            print(f"'{book.title}' is already borrowed!")
                        else:
                            book.mark_as_borrowed()
                            self.borrowed_books.append(book)
                            print(f"'{self.name}' borrowed: '{book.title}'!\nReturn date: '{book.return_date}'")
                    else:
                        print(f"'{self.name}' has already borrowed: '{book.title}'!")
                else:
                    print("This book is not in the library!")
            else:
                print(f"'{self.name}' is not a member!")
        else:
            print(f"'{self.name}' already has borrowed 5 books!")
        

library = load_library(LIBRARY_PATH)


while True:
    first_choice = input("Please enter your desired choice:\n1- Add a book to library\n2- Add a member to library\n" \
    "3- Borrow a book\n4- Return a book\n5- Search a book using title\n6- Search a member using name\n7 -Show all books\n" \
    "8- Show all members\n9- Show number of available books\n10- Upload your library\n11- Save to Library pickle\n12- Quit\nYour choice: ").strip()

    if first_choice == '1':
        while True:
            exists = False

            book_title = input("Please enter the title of the book: ").strip()
            for book in library.books:
                    if book.title == book_title:
                        print(f"'{book_title}' already exists!")
                        exists = True
                        break
            if exists:
                continue
            if not book_title:
                print("The title can not be empty!")
                continue

            book_author = input("Please enter the name of the author: ").strip()
            for book in library.books:
                    if book.author == book_author:
                        print(f"'{book_author}' already exists!")
                        exists = True
                        break
            if exists:
                continue
            if not book_author:
                print("The author name can not be empty!")
                continue

            book_isbn = input("Please enter the book's ISBN: ").strip()
            for book in library.books:
                    if book.isbn == book_isbn:
                        print(f"'{book_isbn}' already exists!")
                        exists = True
                        break
            if exists:
                continue
            if not book_isbn:
                print("ISBN can not be empty!")
                continue

            user_book = Book(book_title, book_author, book_isbn)
            library.add_book(user_book)

            second_choice = input("Do you wish to continue? (y/n): ").strip().lower()
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")

    elif first_choice == '2':
        while True:
            exists = False
            member_name = input("Please enter member's name: ").strip()
            for member in library.members:
                    if member.name == member_name:
                        print(f"'{member_name}' already exists!")
                        exists = True
                        break
            if exists:
                continue
            if not member_name:
                print("The name can not be empty!")
                continue
            try:
                member_id = int(input("Please enter member's ID: "))
                for member in library.members:
                    if member.id == member_id:
                        print(f"'{member_id}' already exists!")
                        exists = True
                        break
                if exists:
                    continue
            except ValueError:
                print("ID must be a number!")
                continue
            if not member_id:
                print("The ID can not be empty!")
                continue
            member_email = input("Please enter member's email: ").strip()
            for member in library.members:
                    if member.email == member_email:
                        print(f"'{member_email}' already exists!")
                        exists = True
                        break
            if exists:
                    continue
            if not member_email:
                print("The email can not be empty!")
                continue

            user_member = Member(member_name, member_id, member_email, [])
            library.add_member(user_member)

            second_choice = input("Do you wish to continue? (y/n): ").strip().lower()
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")
    elif first_choice == '3':
        while True:
            try:
                user_member_id = int(input("Please enter the member ID: "))
            except ValueError:
                print("ID must be a number!")
                continue
            user_book_isbn = input("Please enter the book ISBN: ").strip()

            library.borrow_book(user_member_id, user_book_isbn)

            second_choice = input("Do you wish to continue? (y/n): ").strip().lower()
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")
    
    elif first_choice == '4':
        while True:
            try:
                user_member_id = int(input("Please enter the member ID: "))
            except ValueError:
                print("ID must be a number!")
                continue
            user_book_isbn = input("Please enter the book ISBN: ").strip()

            library.return_book(user_member_id, user_book_isbn)

            second_choice = input("Do you wish to continue? (y/n): ").strip().lower()
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")

    elif first_choice == '5':
        while True:
            title = input("Please enter the title of the book: ").strip()
            library.search_book_by_title(title)

            second_choice = input("Do you wish to continue? (y/n): ").strip().lower()
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")
    
    elif first_choice == '6':
        while True:
            name = input("Please enter the name of the member: ").strip()
            library.search_member_by_name(name)

            second_choice = input("Do you wish to continue? (y/n): ").strip().lower()
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")

    elif first_choice == '7':
        library.show_all_books()

    elif first_choice == '8':
        library.show_all_members()
    
    elif first_choice == '9':
        library.books_status()

    elif first_choice == '10':
        library = load_library()
    
    elif first_choice == '11':
        second_choice = input("Would you like to quick save in an existing path? (y/n): ").strip().lower()
        if second_choice == 'y':
            save_library(library, LIBRARY_PATH)
        elif second_choice == 'n':
            save_library(library)
        else:
            print("Invalid input!")

    elif first_choice == '12':
        save_choice = input("Would you like to save before quitting? (y/n): ").strip().lower()
        if save_choice == 'y':
            second_choice = input("Would you like to quick save in an existing path? (y/n): ").strip().lower()
            if second_choice == 'y':
                save_library(library, LIBRARY_PATH)
            elif second_choice == 'n':
                save_library(library)
            else:
                print("Invalid input!")
        print("Library closed!")
        break

    else:
        print("Invalid input!")