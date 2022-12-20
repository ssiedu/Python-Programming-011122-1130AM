from multipledispatch import dispatch

@dispatch(int,int)
def product(first,second):
    result=first*second
    print("Product of two int value : ",result)

@dispatch(int,int,int)
def product(first,second,third):
    result=first*second*third
    print("Product of three int value : ",result)

@dispatch(int,float)
def product(first,second):
    result=first*second
    print("Product of two different values : ",result)


product(2,3,4)
product(2,2)
product(2,1.1)
product(3,4)
