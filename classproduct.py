class product:
      def getdata(self,a,b):
            self.num1=a
            self.num2=b
      def calculate(self):
            self.result=self.num1*self.num2
      def display(self):
            print("Product of two numbers :",self.result)

p=product()
x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))
p.getdata(x,y)
p.calculate()
p.display()
