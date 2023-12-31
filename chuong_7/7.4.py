from tkinter import *

win = Tk()
win.title("xin chao!")
win.geometry('400x300')

name = Label(win,text="Ten sinh vien:",font=('algerian',15))
name.place(x=0,y=0)
name_1 = Label(win,text="ID sinh vien:",font=('algerian',15))
name_1.place(x=0,y=30)
name_2 = Label(win,text="mat khau:",font=('algerian',15))
name_2.place(x=0,y=60)
name_3 = Label(win)


text_1 = Text(win,width=20,height=1)
text_1.place(x=150,y=4)
text_2 = Text(win,width=20,height=1)
text_2.place(x=150,y=34)
text_3 = Text(win,width=20,height=1)
text_3.place(x=150,y=64)

def click_():
    name_3.config(text='ban vua gui thanh cong thong tin!',fg='red')
    name_3.place(x=140,y=170)
btn = Button(win,text="SEND",bg='red',font=("arial",20),command=click_)
btn.place(x=170,y=100)


    
win.mainloop()
