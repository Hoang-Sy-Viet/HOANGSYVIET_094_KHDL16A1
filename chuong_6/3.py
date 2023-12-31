import threading
import time
def even():
    for num in range(29,51):
        if num % 2 == 0:
            print(num)
            print('đây là thread: {}'.format(threading.current_thread().name))
            time.sleep(1)
def odd():
    for num in range(29,51):
        if num % 2 != 0:
            print(num)
            print('đây là thread: {}'.format(threading.current_thread().name))
            time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=even)
    t2 = threading.Thread(target=odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()