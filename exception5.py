try:
    even_number=[2,4,6,8]
    print("Even Number : ",even_number[5])

except ZeroDivisionError:
    print("Denominator can not be zero")

except IndexError:
    print("Index out of bound")
