class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' with '{self.pages}' pages.'"
    
    def __add__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Value must be a Book!")
        return Book(f"{self.title} & {other.title}", f"{self.author} - {other.author}", self.pages + other.pages)
    
    def __del__(self):
        print(f"'{self.title}' was deleted from memory!")

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Brave New World", "Aldous Huxley", 311)
book3 = Book("Fahrenheit 451", "Ray Bradbury", 249)

combined_book = book1 + book2

print(combined_book)

print(book1)
print(book2)
print(book3)