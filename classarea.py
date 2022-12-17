class Area:
      r=eval(input("Enter radius :"))
      def calculate(self):
            self.a=3.14*self.r*self.r
      def display(self):
            print("Area of circle : ",self.a)

a=Area()
a.calculate()
a.display()
