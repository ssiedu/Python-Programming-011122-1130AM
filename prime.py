num= int(input("Enter any number : "))
flag = 1
for i in range(2,(num+1)//2):
      if(num%i==0):
            flag = 0
            break

if(flag==1):
      print("Number is prime ")
else:
      print("Number is not prime")
