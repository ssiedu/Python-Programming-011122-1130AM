for i in range(1,6):
      for j in range(1,6):
            print(i*j,end=" ")
      print()
print("-------------------------------------")

for i in range(1,6):#1 2 3 4  5
      for j in range(1,i+1):#2 3 4 5 6
            print("*",end=" ")
      print()

print("------------------------------------")

for i in range(65,70):
      for j in range(65,70):
            print(chr(i),end=" ")
      print()
print("----------------------------------------")

for i in range(ord('A'),ord('F')):
      for j in range(ord('A'),i+1):
            print(chr(j),end=" ")
      print()






