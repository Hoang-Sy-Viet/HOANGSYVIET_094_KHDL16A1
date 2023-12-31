class stack:
    # khởi tạo
    def __init__(self,size):
        self.size = size
        self.data =[]
    def display(self):
        print(self.data)
    # phương thức push đưa 1 phần tử vào ngăn xếp
    def push(self,add):
        self.data.append(add)
        return self.data
    # phương thức isempty kiểm tra ngăn xếp có trống hay k
    def isempty(self):
        return len(self.data) ==0
    # def isfull kiểm tra xem ngăn xếp đầy hay chưa
    def isfull(self):
        return len(self.data) == self.size
    #hàm pop lấy ra 1 phần tử từ đỉnh ngăn xếp và xóa nó
    def pop(self):
        if self.isempty():
            print("ngăn xếp trống!")
        else:
            print(self.data.pop())
    #  Xem phần tử đầu tiên trên đỉnh ngăn xếp mà không xóa nó
    def peek(self):
        if self.isempty():
            print("ngăn xếp trống")
        else:
            print(self.data[-1])
    # del phương thức hàm hủy
ngan_xep =stack(3)
ngan_xep.push(1)
ngan_xep.push(2)
ngan_xep.push(3)
ngan_xep.display()
print(ngan_xep.isempty())
print(ngan_xep.isfull())
ngan_xep.pop()
ngan_xep.peek()
ngan_xep.display()

