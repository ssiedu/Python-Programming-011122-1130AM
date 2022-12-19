class First:#First Base Class
    def __init__(self):
        self.x=int(input("Enter the value of x : "))

class Second:#Second Base class
    def getdata(self):
        self.y=int(input("Enter the value of y : "))

class Third(First,Second):#Derive class
    def calculate(self):
        self.add=self.x+self.y
    def display(self):
        print("sum of two numbers : ",self.add)


T=Third()
T.getdata()
T.calculate()
T.display()
