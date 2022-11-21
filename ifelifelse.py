m=eval(input("Enter Marks of mathematics in between(1-100): "))
e=eval(input("Enter marks of English in between(1-100): "))
com=eval(input("Enter marks of Computer in between(1-100) :"))
h=eval(input("Enter Marks of hindi in between(1-100):"))
s=eval(input("Enter Marks of science in between(1-100) :"))
total = m+e+com+h+s
print("Total Number : ",total)
per = total/5
print("Percentage : ",per)
if per>80 and per<=100:
      print("A Grade")
elif per>70 and per<=80:
      print("B Grade")
elif per>60 and per<=70:
      print("C Grade")
elif per>50 and per<=60:
      print("D Grade")
elif per>=40 and per<=50:
      print("E Grade")
else:
      print("Fail")
