class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            raise ValueError("Value must be a BankAccount!")
        if self == other:
            return BankAccount(self.owner, self.balance + other.balance)
        return BankAccount(f"{self.owner} & {other.owner}", self.balance + other.balance)
    
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            raise ValueError("Value must be a BankAccount!")
        return self.owner == other.owner
    
    def __str__(self):
        return f"'{self.owner}': '${self.balance}'"
    
    def __del__(self):
        print(f"'{self.owner}' was deleted from memory!")


acc1 = BankAccount("Alice", 5000)
acc2 = BankAccount("Alice", 2000)
acc3 = BankAccount("Bob", 3000)

print(acc1) 
print(acc3) 

combined1 = acc1 + acc2
print(combined1)  

combined2 = acc1 + acc3
print(combined2)  

print(acc1 == acc2) 
print(acc1 == acc3) 