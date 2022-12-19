class First:#Base class
    def getdata(self):
        self.x=int(input("Enter first value : "))
        self.y=int(input("Enter Second value : "))


class Second(First):#derive class
    def calculate(self):
        self.add=self.x+self.y
        print("sum of two numbers : ",self.add)


s=Second()
s.getdata()
s.calculate()
