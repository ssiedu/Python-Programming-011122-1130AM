import threading
import time
def square(num):
    print("Calculate the square root of given no. ")
    for n in num:
        time.sleep(0.3)
        print("square is : ", n*n)


def cube(num):
    print("Calculate the cube of the given no ")
    for n in num:
        time.sleep(0.3)
        print("Cube is : ",n*n*n)

arr=[3,4,5,2]

#t1=time.time()
#square(arr)
#cube(arr)
th1=threading.Thread(target=square,args=(arr,))
th2=threading.Thread(target=cube,args=(arr,))
th1.start()
time.sleep(0.2)
th2.start()
th1.join()
th2.join()
print("Thank You")




#print("Total time taken by thread is : ", time.time()-t1)
