fout=open("Myfile1.txt","a")
name=input("Enter Name of Student : ")
age =int(input("Enter age of student : "))
per = eval(input("Enter percentage of student : "))
fout.write("Name : "+name+"\n")
fout.write("Age : "+str(age)+"\n")
fout.write("Percentage : "+str(per)+"\n")
fout.close()