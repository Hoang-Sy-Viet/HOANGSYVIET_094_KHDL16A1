class TS:
    d_sach= []
    diem_chuan = 20
    def __init__(self,name,toan,ly,hoa):
        self.name= name
        self.toan= toan
        self.ly= ly
        self.hoa = hoa
    def tong_diem(self):
        tong_diem = self.toan + self.ly +self.hoa
        return tong_diem
    def in_thong_tin_giam_dan(self):
        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("full name","diem toan","diem ly","diem hoa","tong diem"))
        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(self.name,self.toan,self.ly,self.hoa,self.tong_diem()))
                
n = int(input("nhap so thi sinh:"))
for i in range (1,n+1):
    print(f"-----------------nhap thi sinh thu {i}------------------")
    name = input("nhap ten thi sinh:")
    toan = float(input("nhap diem toan:"))
    ly = float(input("nhap diem ly:"))
    hoa = float(input("nhap diem hoa:"))
    thi_sinh = TS(name,toan,ly,hoa)
    TS.d_sach.append(thi_sinh)

TS.d_sach.sort(key=lambda x: x.tong_diem(),reverse=True)
print("______________________Danh Sach Sinh Vien Trung Tuyen________________________")
for t_sinh in TS.d_sach:
    if t_sinh.tong_diem() >= TS.diem_chuan:
        t_sinh.in_thong_tin_giam_dan()
