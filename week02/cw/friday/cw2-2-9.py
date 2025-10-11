import json

book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year_published": 1960,
    "genre": "Fiction",
    "pages": 281,
    "ISBN": "978-0-06-112008-4",
    "publisher": "J.B. Lippincott & Co.",
    "language": "English",
    "available": True
}


with open('cw2-2-9.json', 'w') as file:
    json.dump(book, file)

with open('cw2-2-9.json', 'r') as file:
    read = json.load(file)
    print(read)