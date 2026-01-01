class BankAccount:
    def __init__(self, name, balance):
        self.__balance = balance
        self.name = name

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value + self.__balance < 0 :
            raise ValueError("Your balance whould be empty!")
        self.__balance += value

    @classmethod
    def form_string(cls, data):
        info = data.split(',')
        return cls(info[0], int(info[1]))
    
ali = BankAccount.form_string("Ali,1500")
ali.balance = -300
print(ali.balance)