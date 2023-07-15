class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    def sub(self):
        return self.num1-self.num2
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=Calculator(a,b)
print("addition of two numbers:      ",obj.add())
print("substraction of two numbers:  ",obj.sub())
print("multiplication of two numbers:",obj.mul())
print("division of two numbers:      ",obj.div())