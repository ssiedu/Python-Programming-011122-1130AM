a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))
if(a>b and a>c):
      print(a,"is greater than ",b,"and",c)
elif (b>c):
      print(b,"is greater than ",a,"and",c)
else:
      print(c,"is greater than ",a,"and",b)
