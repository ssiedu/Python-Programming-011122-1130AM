try:
    a=5
    #b=0
    #print(a/b)
    #print(a+b)
    print(b)
except TypeError:
    print("Some Error Occured")
except ZeroDivisionError:
    print("Zero Division Error Occured")
except NameError:
    print("Name error Occured")
print("Out of try and except block")
