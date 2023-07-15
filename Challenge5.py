class Account:  
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    def deposit(self, amount):
        self.balance = self.balance + amount
    def getBalance(self):
        return self.balance
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


demo1 = SavingsAccount("ganesh", 2000, 5)  # initializing a SavingsAccount object
demo1.deposit(500)
print(demo1.getBalance())

demo2 = SavingsAccount("ganesh", 2000, 5)
demo2.withdrawal(500)
print(demo2.getBalance())

demo3 = SavingsAccount("ganesh", 2000, 5) 
print(demo3.interestAmount())