import threading
import random
import numpy as np
n = int(input("nhập số phần tử: "))
thread_list = [random.randint(1,10) for i in range(n)]
total=0
def thread_sum(thread_list):
    global total
    print("Thread 1 : {}".format(thread_list[:10]))
    for i in range(0,len(thread_list[:10])):
        total += thread_list[i]
number_of_list = [thread_list[i:i+10] for i in range(0, len(thread_list), 10)]
def main():
    
    for i in number_of_list:
        t = threading.Thread(target=thread_sum, args=(i,))
        t.start()
        t.join()
if __name__ == "__main__":
    main()
    print(total)

