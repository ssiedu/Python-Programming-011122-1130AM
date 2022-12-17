class Addition:
      def getdata(self):
            self.num1=int(input("Enter First number : "))
            self.num2=int (input("Enter Second number : "))
      def add(self):
            self.add=self.num1+self.num2
      def display(self):
            print("Addition is : ", self.add)

a=Addition()
a.getdata()
a.add()
a.display()
