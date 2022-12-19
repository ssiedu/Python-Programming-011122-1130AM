class First:#Base class
    def __init__(self):
        self.x=int(input("Enter the value of x : "))
        self.y=int(input("Enter the value of y : "))

class Second(First):#First derive class
    def getSum(self):
        self.add=self.x+self.y
    def display(self):
        print("Sum of two numbers : ", self.add)


class Third(First):#Second derive class
    def getMul(self):
        self.mul=self.x*self.y
    def display(self):
        print("mul of two numbers : ", self.mul)



S=Second()
S.getSum()
S.display()
T=Third()
T.getMul()
T.display()
