fout=open("Myfile2.txt","w")
for i in range(5):
    name=input("Enter name of student : ")
    fout.write(name+"\n")
fout.close()
