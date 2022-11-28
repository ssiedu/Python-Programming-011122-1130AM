num = int (input("Enter Any Number : "))
temp = num
rev =0
sum1=0
tod=0
while(num!=0):
      rev = rev *10 + num%10 # rec 32*10 + 1%10 320+1 = 321
      sum1= sum1+num%10
      tod = tod+1
      num = num//10# 123//10=  12  12//10 =1
      
print("Reverse Number is : ",rev)
print("Sum of Digit  : ", sum1)
print("Total Number of digit : ", tod)

if(temp==rev):
      print("Number is pallindrome")
else:
      print("Number is not pallindrome")
