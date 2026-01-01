class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def __len__(self):
        return len(self.books)
    
    def __add__(self, other):
        if not isinstance(other, Library):
            raise ValueError("Value must be a Library!")
        return Library(self.books + other.books)
    
    def __str__(self):
        if not self.books:
            return "The library is empty."
        book_list = "\n".join(f"{i+1}. {book}" for i, book in enumerate(self.books))
        return f"Library contains:\n{book_list}"
        
    def __del__(self):
        print("Library deleted!")


library1 = Library(["Harry Potter", "Lord of the Rings"])
library2 = Library(["Bostan", "Golestan"])

library3 = library1 + library2

print(library3)
