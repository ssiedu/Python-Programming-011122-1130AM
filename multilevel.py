class First:#Base class
    def __init__(self):
        self.x=int(input("Enter first number : "))
        self.y=int(input("Enter second number : "))

#Intermediate class(Base class for Third / Derive class for First)
class Second(First):
    def calculate(self):
        self.add=self.x+self.y


class Third(Second):#derive class
    def display(self):
        print("Sum is : ", self.add)


T=Third()
#T.getdata()
T.calculate()
T.display()
