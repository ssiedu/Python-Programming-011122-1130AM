try:
    num=int(input("Enter a number : "))
    assert num%2==0
    assert num>0

except:
    print("Not an even Number or negative number")

else:
    reci=1/num
    print("reciprocal of number ",reci)
