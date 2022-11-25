num1=eval(input("Enter First Number : "))
num2=eval(input("Enter Second Number : "))
ch=input("Enter Symbol like (+,-,*,/):")
match ch:
      case '+':
            print("Addition : ", num1+num2)
      case '-':
            print("Subtraction : ",num1-num2)
      case '*':
            print("Multiplication : ", num1*num2)
      case '/':
            print("Division : ", num1/num2)
      case _:
            print("Please Enter valid choice")
