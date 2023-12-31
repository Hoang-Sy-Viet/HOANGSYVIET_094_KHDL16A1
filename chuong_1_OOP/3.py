class PS:
    def __init__(self,tu_so,mau_so):
        self.tu_so= tu_so
        self.mau_so= mau_so
    def kiem_tra(self):
        if self.mau_so == 0:
            return False
        else:
            return True
    def in_phan_so(self):
        print("phan so vua dc nhap la: ",end="")
        print(f"{self.tu_so}/{self.mau_so}")
    def nhap_phan_so(self):
        self.tu_so= int(input("nhap tu so:"))
        self.mau_so= int(input("nhap mau so:"))
phan_so = PS(0,1)
phan_so.nhap_phan_so()
if phan_so.kiem_tra():
    phan_so.in_phan_so()
else:
    print("phan so khong hop le!!")
    