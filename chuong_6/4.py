import threading
def giai_thua(n):
    if n == 0:
        return 1
    return n*giai_thua(n-1)
def hien_thi():
    print(giai_thua(n))
if __name__ == '__main__':
    n = int(input("Nhập số cần tính giai thừa: "))
    t = threading.Thread(target=giai_thua,args=(n,))
    t2 = threading.Thread(target=hien_thi)
    t.start()
    t2.start()
    t.join()
    t2.join()