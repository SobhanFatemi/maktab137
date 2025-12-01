class Book:
    pages = []
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
    def __len__(self):
        return len(self.pages)
    
    def __getitem__(self, index):
        return self.pages[index]
    
    def __setitem__(self, index, content):
        self.pages[index] = content
    
    def __delitem__(self, index):
        del self.pages[index]

    def __contains__(self, keyword):
        for page in self.pages:
            words = page.split()
            for word in words:
                if word == keyword:
                    return True
        return False
    
book = Book("The Catcher in the Rye", "J.D. Salinger")
book.pages = ["Page 1 content", "Page 2 content", "Page 3 content"]
print(book)

print(len(book))
print(book[2])

book[2] = "Updated content for page 3"
print(book[2])

del book[1]
print(len(book))

print("Catcher" in book)
print("content" in book)