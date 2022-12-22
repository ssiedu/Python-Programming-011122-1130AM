file=open("Myfile1.txt","r")
while str:
    str=file.readline()
    print(str)

file.close()
