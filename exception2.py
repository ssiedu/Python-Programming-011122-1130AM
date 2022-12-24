try:
    print("Try Block")
    x=int(input("Enter First Number : "))
    y=int(input("Enter Second Number : "))
    z=x/y

except ZeroDivisionError:
    print("Except ZeroDivisionError Block")
    print("Division by Zero not allowed")

except ValueError:
    print("Value Error Occured")

else:
    print("Else Block")
    print("value of z : ",z)

finally:
    print("Finally Block")


print("Out of try,except,else and finally")
