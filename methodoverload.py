class Area:
    def findArea(self,a=None,b=None):
        if(a!=None and b!=None):
            print("Area of Rectangle : ",a*b)
        elif(a!=None):
            print("Area of square : ",a*a)
        else:
            print("nothing")


a=Area()
a.findArea()
a.findArea(2)
a.findArea(2,3)
