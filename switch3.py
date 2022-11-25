ch=input("Enter String : ")
match ch:
      case 'm':
            print("Monday")
      case 't':
            print("Tuesday")
      case 'w':
            print("Wednesday")
      case 'th':
            print("Thursday")
      case 'f':
            print("Friday")
      case 's':
            print("Saturday")
      case 'sun':
            print("Sunday")
      case _:
            print("Invalid Choice")
