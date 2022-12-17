class Student:
      def __init__(self,name=None,age=None,rollno=None):
            self.name=name
            self.age=age
            self.rollno=rollno
      def display(self):
            print("Student name : ", self.name)
            print("Student age  : ", self.age)
            print("Student rollno: ", self.rollno)

s=Student()
s.display()
s1=Student("Ram",22,101)
s1.display()
s2=Student(age=22,rollno=101)
s2.display()
