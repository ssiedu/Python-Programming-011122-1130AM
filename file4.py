data=int(input("How many Students are there in the class : "))
fout=open("Student.txt","w")
for i in range(data):
    print("Enter Details for student ",i+1)
    rollno=int(input("Enter roll no of student : "))
    name = input("Enter name of student : ")
    per = eval(input("Enter Percentage of student : "))
    rec = str(rollno) +" , " +name+" , "+str(per)+"\n"
    fout.write(rec)
fout.close()
