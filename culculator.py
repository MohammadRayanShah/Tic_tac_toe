from tkinter import *
from tkinter import ttk


def add():

   obj1=entry1.get()
   obj2=entry2.get()
   sum=int(obj1)+int(obj2)
   text.set(int(sum))

def subtract():

    obj1=entry1.get()
    obj2=entry2.get()
    sub=int(obj1)-int(obj2)
    text.set(int(sub))

def multiply():

    obj1=entry1.get()
    obj2=entry2.get()
    product=int(obj1)*int(obj2)
    text.set(int(product))

def division():

    obj1=entry1.get()
    obj2=entry2.get()
    ans=int(obj1)/int(obj2)
    text.set(float(ans))

def delete():

    entry1.delete(0,END)
    entry2.delete(0, END)

root=Tk()

entry1=Entry(root)
entry1.pack()

entry2=Entry(root)
entry2.pack()

ttk.Button(root,text="Add",command = add).pack()

ttk.Button(root,text="Subtract",command = subtract).pack()

ttk.Button(root,text="Multiply",command = multiply).pack()

ttk.Button(root,text="Division",command = division).pack()

ttk.Button(root,text="Clear",command = delete).pack()

text = StringVar()
text.set('0')
label = Label(root,textvariable = text)
label.pack()


root.mainloop()