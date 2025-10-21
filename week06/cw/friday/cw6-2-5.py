class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enought credit!")
        else:
            self.balance += amount
    
    def display_balance(self):
        print(f"Your balance is: {self.balance}")

class Bank:
    def __init__(self, name, accounts=[]):
        self.name = name
        self.accounts = accounts

    def create_account(self, *args):
        exists = False
        for arg in args:
            for account in self.accounts:
                    if account.account_number == arg.account_number:
                        print(f"'{arg.account_number}' already exist!")
                        exists = True
            if not exists:
                self.accounts.append(arg)
                print(f"'{arg.account_number}' was added!")
                

    def close_account(self, number):
        found = False
        for account in self.accounts:
            if account.account_number == number:
                found = True
                self.accounts.remove(account)
                print(f"'{account.account_number}' was successfully removed.")
        if not found:
            print(f"no account with the account number of '{number}' was found!")

    def update_balance(self, number, action, amount):
        found = False
        for account in self.accounts:
            if account.account_number == number:
                found = True
                if action == 'deposit':
                    account.deposit(amount)
                elif action == 'withdraw':
                    account.withdraw(amount)
                else:
                    print("Invalid input!")   
        if not found:
            print(f"no account with the account number of '{number}' was found!")
    
    def display_accounts(self):
        for account in self.accounts:
            print(f"\nAccount number: {account.account_number}\nAccount balance: {account.balance}\n")

sobhan = BankAccount(6219861912345678, 500)
arman = BankAccount(6219861909876543, 1000)
bahman = BankAccount(6219861993873619, 100)

saman = Bank("Saman Bank")
saman.create_account(sobhan, arman, bahman)
saman.close_account(6219861912345678)
saman.update_balance(6219861909876543, 'deposit', 200)
saman.update_balance(6219861993873619, 'withdraw', 200)
saman.display_accounts()