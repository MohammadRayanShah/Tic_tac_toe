from tkinter import *
def show():
    print(radval.get())
root= Tk()
radval=IntVar()

Label(root,text='Choose your course ').pack()
Radiobutton(root, text='BCA',value = 1, variable = radval).pack()
Radiobutton(root, text='BBA',value = 2, variable = radval).pack()
Radiobutton(root, text='Bcom',value = 3, variable = radval).pack()
Button(root,text = 'show value ',command = show).pack()
root.mainloop()