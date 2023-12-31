class Stack:
    def __init__(self,size):
        self.size = size
        self.data =[]
    def push(self,add):
        self.data.append(add)
    def count__(self):
        print(f"số phần tử trên ngăn xếp là :{len(self.data)}")
st = Stack(3)
st.push(1)
st.push(2)
st.push(3)
st.count__()