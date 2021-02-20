from tkinter import *
def show():
    text.set(entry.get())
def clear():
    entry.delete(0,END)
root = Tk()

entry=Entry(root , bg = 'red',fg = 'black')
entry.pack()
Button(root,text ='Show in the label' , command = show).pack()
Button(root,text = 'clear',command = clear).pack()
text = StringVar()
text.set('---')
label = Label(root,textvariable = text)
label.pack()
root.mainloop()