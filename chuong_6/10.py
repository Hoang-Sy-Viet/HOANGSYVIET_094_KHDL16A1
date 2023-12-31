import threading
import random
n = int(input("nhập số phần tử: "))
list_thread = [random.randint(1,100) for i in range(n)]
def thread_max(list_thread):
    print(list_thread)
    max = list_thread[0]
    for i in range(0,len(list_thread)):
        if list_thread[i] > max:
            max = list_thread[i]
    print("phần tử lớn nhất cả list",max)
number_list = [list_thread[i:i+10] for i in range(0, len(list_thread), 10)]
def main():
    for i in number_list:
        t = threading.Thread(target=thread_max, args=(i,))
        t.start()
        t.join()
if __name__ == "__main__":
    main()