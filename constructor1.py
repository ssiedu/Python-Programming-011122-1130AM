#Non-parametrized constructor
class Addition:
      def __init__(self):
            self.num1=int(input("Enter First value : "))
            self.num2=int(input("Enter Second value : "))
      def calculate(self):
            self.add=self.num1+self.num2
      def print(self):
            print("First value : ",self.num1)
            print("Second value : ",self.num2)
            print("sum is : ",self.add)


a=Addition()
a.calculate()
a.print()
