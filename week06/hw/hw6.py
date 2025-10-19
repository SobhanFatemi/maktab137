import pickle
from datetime import datetime, timedelta

LIBRARY_PATH = "library_data.pkl"

def save_library(library, path):
    with open(path, "wb") as f:
        pickle.dump(library, f)
    print("Library data saved successfully.")

def load_library(path):
    try:
        with open(path, "rb") as file:
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
        

# library = Library([], [])

# harry_potter = Book("Harry Potter", "J. K. Rowling", "0-7701-8798-6")
# lotr = Book("The Lord of the Rings", "J. R. R. Tolkien", "0-395-19395-8")
# hobbit = Book("The Hobbit", "J. R. R. Tolkien", "0-618-00221-9")
# got = Book("A Game of Thrones", "George R. R. Martin", "0-553-10354-7")
# mockingbird = Book("To Kill a Mockingbird", "Harper Lee", "0-06-112008-1")
# gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", "0-7432-7356-7")
# nineteen_eighty_four = Book("1984", "George Orwell", "0-452-28423-6")
# moby_dick = Book("Moby Dick", "Herman Melville", "0-14-243724-7")
# pride_prejudice = Book("Pride and Prejudice", "Jane Austen", "0-19-280238-0")
# catcher_rye = Book("The Catcher in the Rye", "J. D. Salinger", "0-316-76948-7")
# brave_new_world = Book("Brave New World", "Aldous Huxley", "0-06-085052-3")

# john = StudentMember("John", 4001223013, "John55@gmail.com", [])
# steve = StudentMember("Steve", 4001223012, "Steve23@gmail.com", [])
# michael = StudentMember("Michael", 4001223014, "michael99@gmail.com", [])
# emily = StudentMember("Emily", 4001223015, "emily77@gmail.com", [])
# david = StudentMember("David", 4001223016, "david01@gmail.com", [])
# sophia = StudentMember("Sophia", 4001223017, "sophia65@gmail.com", [])
# daniel = StudentMember("Daniel", 4001223018, "daniel42@gmail.com", [])
# olivia = StudentMember("Olivia", 4001223019, "olivia33@gmail.com", [])
# james = StudentMember("James", 4001223020, "james88@gmail.com", [])
# ava = StudentMember("Ava", 4001223021, "ava21@gmail.com", [])
# liam = StudentMember("Liam", 4001223022, "liam14@gmail.com", [])

# rose = TeacherMember("Rose", 3000928394, "rose98@gmail.com", [])
# william = TeacherMember("William", 3000928395, "william83@gmail.com", [])
# natalie = TeacherMember("Natalie", 3000928396, "natalie72@gmail.com", [])

# library.add_book(harry_potter, lotr, hobbit, got, mockingbird, gatsby, nineteen_eighty_four, moby_dick, pride_prejudice, catcher_rye, brave_new_world)
# library.add_member(john, steve, michael, emily, david, sophia, daniel, olivia, james, ava, rose, liam, william, natalie)

# save_library(library)
    
library = load_library(LIBRARY_PATH)

while True:
    first_choice = input("Please enter your desired choice:\n1- Add a book to library\n2- Add a member to library\n" \
    "3- Borrow a book\n4- Return a book\n5- Search a book using title\n6- Search a member using name\n7 -Show all books\n" \
    "8- Show all members\n9- Show number of available books\n10- Upload your library\n11- Save to Library pickle\n12- Quit\nYour choice: ")

    if first_choice == '1':
        while True:
            book_title = input("Please enter the title of the book: ")
            if not book_title:
                print("The title can not be empty!")
                continue
            book_author = input("Please enter the name of the author: ")
            if not book_author:
                print("The author name can not be empty!")
                continue
            book_isbn = input("Please enter the book's ISBN: ")
            if not book_isbn:
                print("ISBN can not be empty!")
                continue

            user_book = Book(book_title, book_author, book_isbn)
            library.add_book(user_book)

            second_choice = input("Do you wish to continue? (y/n): ")
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")

    elif first_choice == '2':
        while True:
            member_name = input("Please enter member's name: ")
            if not member_name:
                print("The name can not be empty!")
                continue
            try:
                member_id = int(input("Please enter member's ID: "))
            except ValueError:
                print("ID must be a number!")
                continue
            if not member_id:
                print("The ID can not be empty!")
                continue
            member_email = input("Please enter member's email: ")
            if not member_email:
                print("The email can not be empty!")
                continue

            user_member = Member(member_name, member_id, member_email, [])
            library.add_member(user_member)

            second_choice = input("Do you wish to continue? (y/n): ")
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
            user_book_isbn = input("Please enter the book ISBN: ")

            library.borrow_book(user_member_id, user_book_isbn)

            second_choice = input("Do you wish to continue? (y/n): ")
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
            user_book_isbn = input("Please enter the book ISBN: ")

            library.return_book(user_member_id, user_book_isbn)

            second_choice = input("Do you wish to continue? (y/n): ")
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")

    elif first_choice == '5':
        while True:
            title = input("Please enter the title of the book: ")
            library.search_book_by_title(title)

            second_choice = input("Do you wish to continue? (y/n): ")
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")
    
    elif first_choice == '6':
        while True:
            name = input("Please enter the name of the member: ")
            library.search_book_by_title(name)

            second_choice = input("Do you wish to continue? (y/n): ")
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
        while True:
            try:
                user_path = input("Please enter your desired path: ")
                load_library(user_path) 
            except Exception as e:
                print(f"An error occured!: {e}")

            second_choice = input("Do you wish to continue? (y/n): ")
            if second_choice == 'y':
                continue
            elif second_choice == 'n':
                break
            else:
                print("Invalid input!")
    
    elif first_choice == '11':
        second_choice = input("Are you sure about the save? (y/n): ")
        if second_choice == 'y':
            save_library(library, LIBRARY_PATH)
        elif second_choice == 'n':
            pass
        else:
            print("Invalid input!")

    elif first_choice == '12':
        break

    else:
        print("Invalid input!")