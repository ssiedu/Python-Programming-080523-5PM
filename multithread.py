import threading
import time
def square(num):
    for i in num:
        time.sleep(1)
        print("Square :",i*i)


def cube(num):
    for i in num:
        time.sleep(1)
        print("Cube :",i*i*i)


l1=[2,3,4,5]
t1=threading.Thread(target=square,args=(l1,))
t2=threading.Thread(target=cube,args=(l1,))
t1.start()
time.sleep(0.5)
t2.start()
t1.join()
t2.join()
print("Thank you")
