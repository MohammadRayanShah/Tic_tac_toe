from tkinter import *
from tkinter import messagebox

def buttontapped():

    messagebox._show('Alert','Its a good day to die hard!')

root = Tk()

Button(root, text="Click me!", command = buttontapped ).pack()

root.mainloop()