import random
while True:
    data=input('''
Game Start....
1.Yes(y|Y)
2.No|Exit(n|N)
''')
    if data.lower()=='y':
        Cnumber=random.randrange(1,6)
        Userinput=int(input("Enter Your Number : "))
        if Userinput > Cnumber:
            print("Computer Number : ",Cnumber)
            print("Your Guess Number is too high ")

        elif Cnumber > Userinput:
            print("Computer Number : ",Cnumber)
            print("Your Guess Number is too low ")

        else:
            print("Computer Number : ", Cnumber)
            print("Your Guess Number is equal ")
    else:
        break
        
   


