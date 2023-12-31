import threading
import time
def chan():
    for i in range(30):
        if i %2 ==0:
            print(i)
            time.sleep(1)
def le():
    for i in range(30):
        if i %2 !=0:
            print(i)
            time.sleep(1.1)
if __name__=='__main__':
    t1 = threading.Thread(target=chan)
    t2 = threading.Thread(target = le)
    t1.start()
    t2.start()
    t1.join()
    t2.join()