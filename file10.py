import pickle
file=open("Binary.dat","wb")
x=[10,20,30,40,50]
pickle.dump(x,file)
file.close()
with open("Binary.dat","rb")as file:
    data=pickle.load(file)
    print(data)
file.close()

