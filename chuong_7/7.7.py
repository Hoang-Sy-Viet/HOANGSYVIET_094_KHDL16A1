from tkinter import *

win = Tk()
win.title("hello!")
win.geometry('400x300')

name_1 = Label(win,text="Enter Value of Integer N:",fg='red').place(x=0,y=0)
entry_ = Entry(win).place(x=140,y=0)

def click_():
    name = Label(win,text='the sum is 1 +....+')
    name.place(x=70,y=130)
btn  = Button(win,text="Validate",font=('arial',20),fg='red',command=click_)
btn.place(x=80,y=50)
win.mainloop()