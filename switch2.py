ch=input("Enter your choice \n 1. pos/neg(PN) \n 2.Even/Odd(EO) \n")
match ch:
      case "PN":
            num=int(input("Enter any number: "))
            if(num>0):
                  print("Positive")
            else:
                  print("Negative")
      case "EO":
            num=int(input("Enter any Number: "))
            if(num%2==0):
                  print("Even")
            else:
                  print("Odd")
            
