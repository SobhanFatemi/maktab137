BOOKS = (
    (1, "The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fiction", True),
    (2, "1984", "George Orwell", 1949, "Science Fiction", True),
    (3, "The Wealth of Nations", "Adam Smith", 1776, "Economics", False),
    (4, "Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, "History", True),
    (5, "2", "Paulo Coelho", 1988, "Fiction", True),
    (6, "One Hundred Years of Solitude", "Gabriel García Márquez", 1967, "Fiction", False),
    (7, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy", True),
    (8, "Mein Kampf", "Adolf Hitler", 1925, "History", True),
    (9, "Rich Dad Poor Dad", "Robert Kiyosaki", 1997, "Economics", True),
    (10, "The Divan of Hafez", "Hafez Shirazi", 1390, "Poetry", True)
)

basket = []

def get(book_tuple):
    books = []
    for book in book_tuple:
        books.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "publish_date": book[3],
            "genre": book[4],
            "is_available": book[5]

        })
    return books

def show_all(books):
    for i, book in enumerate(books):
        print(f"#{i+1}: {book['title']}")

def show_available(books):
    i=0
    for book in books:
        if book["is_available"] == True:
            i+=1
            print(f"#{i}: {book['title']}")
    
    if i == 0:
        print("No books available at this moment!")

def show_published(books):
    i=0
    for book in books:
        if book["is_available"] == True:
            i+=1
            print(f"#{i}: {book['title']} published in: {book['publish_date']}")
    
    if i == 0:
        print("No books available at this moment!")

def show_id(books):
    i=0
    for book in books:
        if book["is_available"] == True:
            i+=1
            print(f"#{i}: {book['title']}'s ID is: {book['id']}")
        
    if i == 0:
        print("No books available at this moment!")

def sort(books, based="id", reverse=False):           
    sorted_books = sorted(books, key=lambda book: book[based], reverse=reverse)
    return sorted_books

def lend(books, book_name):
    found = False
    for book in books:
        if book['title'] == book_name:
            found = True
            if book["is_available"] == False:
                print(f"'{book['title']}' is not available at this moment.")
                break
            else:
                basket.append(book)
                book["is_available"] = False
                print(f"'{book['title']}' successfully added to your basket!")
                break
    if not found:
        print(f"'{book_name}' was not found!")

def remove_book(basket, books, book_name):
    found = False
    for lent in basket:
        if lent["title"] == book_name:
            found = True
            basket.remove(lent)
            print(f"'{book_name}' successfully removed from your basket!")
            for book in books:
                if book["title"] == book_name:
                    book["is_available"] = True
                    break
            break
    if not found:
        print(f"'{book_name}' was not found!")
        
                
books = get(BOOKS)
while True:
    first_action = input("Enter your desired action:\n1- Show all the books\n2- Show all available books\n3- Lend books\n4- Sort books\n5- Quit\nYour choice: ")
    
    if first_action == '1':
        show_all(books)
    
    elif first_action == '2':
        show_available(books)

    elif first_action == '3':
        while True:
            second_action = input("Enter your desired action:\n1- Show all available books\n2- Lend a book\n3- Remove an item from your basket\n4- Show basket\n5- Quit\nYour choice: ")
            if second_action == '1':
                show_available(books)
            
            elif second_action == '2':
                book_choice = input("Please enter the name of the book you want to lend: ")
                lend(books, book_choice)

            elif second_action == '3':
                remove_choice = input("Please enter the name of the book you want to remove from your basket: ")
                remove_book(basket, books, remove_choice)
            elif second_action == '4':
                i=0
                for book in basket:
                    i+=1
                    print(f"#{i}: {book['title']}")
                if i == 0:
                    print("Your basket is empty!")

            elif second_action == '5':
                break
            
            else:
                print("Incorrect input!")

    elif first_action == '4':
        while True:
            based = input("In what order do you want to sort:\n1- ID\n2- Published date\n3- Quit\nYour choice: ")
            if based == '3':
                break
            reverse_choice = input("Do you want it reversed? (y/n): ")

            if reverse_choice == 'y':
                reverse = True
            elif reverse_choice == 'n':
                reverse = False
            else:
                print("Invalid input!")
                continue

            if based == '1':
                books = sort(books, "id", reverse)
                show_id(books)
            elif based == '2':
                books = sort(books, "publish_date", reverse)
                show_published(books)
            else:
                print("Invalid input!")
                continue

    elif first_action == '5':
        break

    else:
        print("Incorrect input!")