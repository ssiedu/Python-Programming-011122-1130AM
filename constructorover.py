class Student:
      def __init__(self,name=" ",rollno=None):
            self.name=name
            self.rollno=rollno
      def __init__(self):
            self.name="Ram"
            self.age=22
      def display(self):
            print("student name : ", self.name)
            print("student rollno : ",self.rollno)
            print("Student age : ", self.age)

s=Student()
s.display()
            
