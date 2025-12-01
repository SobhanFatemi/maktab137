import json
import os

class Account:
    def __init__(self, owner, balance, transactions=None):
        if transactions is None:
            transactions = []
        self.owner = owner
        self.balance = balance
        self.transactions = transactions
        self.db_manager = DBManager()
        self.db_manager.set(self.owner, {
            "balance": self.balance,
            "transactions": self.transactions
        })

    def check_credit(self, amount):
        data = self.db_manager.get(self.owner)
        if amount > data["balance"]:
            print("Not enough credit!")
            return False
        return True

    def withdraw(self, amount):
        if self.check_credit(amount):
            self.balance -= amount
            self.db_manager.set(self.owner, {
                "balance": self.balance,
                "transactions": self.transactions
            })

    def deposit(self, amount):
        self.balance += amount
        self.db_manager.set(self.owner, {
            "balance": self.balance,
            "transactions": self.transactions
        })

    def transfer(self, target, amount):
        if self.check_credit(amount):
            self.withdraw(amount)
            target.deposit(amount)



class DBManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    self.data = json.load(file)
                except json.JSONDecodeError:
                    self.data = {}
        else:
            self.data = {}

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()


acc1 = Account("Sobhan", 1000)
acc2 = Account("Khosro", 2000)