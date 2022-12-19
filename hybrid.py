class First:
    def __init__(self):
        self.x=int(input("Enter First Number : "))
        self.y=int(input("Enter Second Number : "))


class Second(First):
    def getSum(self):
        self.add=self.x+self.y


class Third:
    def getdata(self):
        self.a=int(input("Enter First Number : "))
        self.b=int(input("Enter Second Number : "))
    def getMul(self):
        self.mul=self.a*self.b
        
class child(Second,Third):
    def display(self):
        print("Sum of two numbers : ",self.add)
        print("Mul of two numbers : ",self.mul)


c=child()
c.getSum()
#c.display()
c.getdata()
c.getMul()
c.display()

        
