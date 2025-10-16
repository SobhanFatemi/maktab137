class Book:
    def __init__(self, title, author, genre, available):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def borrow(self):
        if self.available:
            print(f"{self.title} was borrowed!")
            self.available = False
        else:
            print(f"{self.title} is not available!")

harry_potter = Book("Harry Potter", "J. K. Rowling", "Fantacy", True)

harry_potter.borrow()
harry_potter.borrow()
