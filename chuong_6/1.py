import threading
def task(n):
    for i in range(1000):
        n+=1
    print(n)
    print("kết thúc luồng: {}".format(threading.current_thread().name))
def thread2(a):
    for i in range(300):
        a*=2
    print(a)
    print("kết thúc luồng: {}".format(threading.current_thread().name))
if __name__ == '__main__':
    t1 = threading.Thread(target=task,args=(10,))
    t2 = threading.Thread(target=thread2,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
