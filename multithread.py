from time import sleep
from threading import *
class Welcome(Thread):
    def run(self):
        for i in range(5):
            print("Welcome")
            sleep(0.5)

class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(0.5)


t1=Welcome()
t2=Hii()
t2.start()
sleep(0.2)
t1.start()
#t1.run()
#t2.run()
t1.join()
t2.join()
print("Hello Everyone")
