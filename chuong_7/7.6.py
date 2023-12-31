from tkinter import *
from tkinter.ttk import *

win = Tk()
win.title("hello!")
win.geometry('400x300')

name_1 = Label(win,text="Enter a Word:").place(x=0,y=0)
entry_ = Entry(win,textvariable=StringVar).place(x=80,y=0)
def click_():
    name = Label(win, text=''+ entry_.get(),font=("arial",15))
    name.place(x=60,y=100)
btn  = Button(win,text="Validate",command=click_)
btn.place(x=80,y=50)
win.mainloop()