def number(**num):
      print(num)

number(num1=10,num2=20)


def printinfo(**kwarg):
      print(kwarg)
      print(kwarg['age'])
      print(kwarg['name'])

printinfo(name='Ssi',age=30)
