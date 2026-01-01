class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def change_address(self):
        new_address = input("Please enter your new address: ")
        self.address = new_address
        print(f"Your new address is: {self.address}")


ali = Person("Ali", 25, "Vanak")
ali.introduce()
ali.change_address()