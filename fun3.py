def simple_interest():
      p=eval(input("Enter principle amount :"))
      r=eval(input("Enter rate of interest : "))
      t=eval(input("Enter time in year : "))
      si=(p*r*t)/100
      print("Simple Interest : ",si)
      total_amount= p+si
      print("Total amount : ", total_amount)
      

simple_interest()
