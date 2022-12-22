import pickle
class Student:
    def __init__(self,rno=0,name=" "):
        self.rno=rno
        self.name=name
        self.s1,self.s2,self.s3=0.0,0.0,0.0;
    def readMarks(self):
        print("Enter Marks of three Subject : ")
        self.s1=eval(input("Enter Marks of sub1 : "))
        self.s2=eval(input("Enter Marks of sub2: "))
        self.s3=eval(input("Enter Marks of Sub3: "))
    def display(self):
        print("Roll No : ", self.rno)
        print("Name : ", self.name)
        print("Subject1 : ",self.s1)
        print("Subject2 : ",self.s2)
        print("Subject3 : ",self.s3)


S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.readMarks()
S2.readMarks()
fout=open("Record","wb")
pickle.dump(S1,fout)
pickle.dump(S2,fout)
fout.close()
fin=open("Record","rb")
try:
    while True:
        s=pickle.load(fin)
        s.display()
except:
    fin.close()







