class ContactBook:
    def __init__(self, contacts=None):
        if contacts is None:
            contacts = {}
        self.contacts = contacts

    def __len__(self):
        return len(self.contacts)

    def __add__(self, other):
        if not isinstance(other, ContactBook):
            raise ValueError("Value must be a ContactBook!")
        new_contacts = {**self.contacts, **other.contacts}
        return ContactBook(new_contacts)
    
    def __str__(self):
        if not self.contacts:
            return "Contact book is empty."
        return ", ".join(self.contacts.keys())

    def __del__(self):
        print("Contact book deleted!")



book1 = ContactBook({"Reza": "09123456789", "Sara": "09129876543"})
book2 = ContactBook({"Ali": "09151112233", "Nazanin": "09163334455"})

book3 = book1 + book2

print(book3)