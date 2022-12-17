class Student:
      name =input("Enter name of student : ")
      age = int(input("Enter age of student : "))
      rollno=int(input("Enter roll no of student : "))
      per = eval(input("Enter percentage of student : "))
      def display(self):
            print("Student name : ",self.name)
            print("Student Age  : ",self.age)
            print("Student roll no : ", self.rollno)
            print("Student percentage : ", self.per)


s=Student()
s.display()
