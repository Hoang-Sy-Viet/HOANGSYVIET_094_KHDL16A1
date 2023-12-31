class Stack:
    def __init__(self,size):
        self.size = size
        self.data =[]
    def push(self,add):
        self.data.append(add)
    def print_stack(self):
        print(f"nội dung của stack là:{self.data}")
st= Stack(3)
st.push(1)
st.push(2)
st.push(3)
st.print_stack()