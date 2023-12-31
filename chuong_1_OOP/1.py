class hcn_:
    " -------------Thong tin hinh chu nhat--------"
    def __init__(self,a,b):
        self.a= a
        self.b= b
        self.S= a*b
        self.V= (a+b)*2
    def inf_(self):
        print("---------------------------")
        print(f"chieu dai hcn = {self.a}   ")
        print(f"chieu rong hcn = {self.b}")
        print(f"chu vi hcn = {self.V}       ")
        print(f"dien tich hcn = {self.S}    ")
tt= hcn_(a=int(input("nhap chieu dai:")),b=int(input("nhap chieu rong:")))
tt.inf_()
print()
print(tt.__doc__)
print(tt.__dict__)