from tkinter import *
root= Tk()
def colorred():
    labeltext.set('colour changed to Red')
    label.config(bg='red')

def colororange():
    labeltext.set('colour changed to orange')
    label.config(bg='orange')

def colorgreen():
    labeltext.set('colour changed to green')
    label.config(bg='green')
labeltext = StringVar()
labeltext.set('label')
label=Label(root, textvariable = labeltext)
label.pack()
Button(root , text= 'Click here!' , command = colorred ).pack()
Button(root , text= 'Click here!' , command = colororange ).pack()
Button(root , text= 'Click here!' , command = colorgreen ).pack()
root.mainloop()