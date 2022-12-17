class Product:
      def __init__(self,a,b,c):
            self.num1=a
            self.num2=b
            self.num3=c
      def calculate(self):
            self.result=self.num1*self.num2*self.num3
      def display(self):
            print("Product of three numbers : ", self.result)


p=Product(2,3,4)
p.calculate()
p.display()
q=Product(1,5,6)
q.calculate()
q.display()
