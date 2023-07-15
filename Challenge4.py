class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

obj=SavingsAccount("ganesh",5000,5)
print("title:",obj.title)
print("balance:",obj.balance)
print("interestRate:",obj.interestRate)