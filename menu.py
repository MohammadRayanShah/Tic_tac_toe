from tkinter import *
def openclick():
    print('Opened successfully')

def close():
    exit()

def undo():
        print('undo successful')

def redo():
    print('redo successful')

def cut():
    print('Cutted')

def copy():
    print('copied successfully')

def paste():
    print('pasted successfully')

root=Tk()

menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu,tearoff=0)
menu.add_cascade(label='file',menu=subMenu)
subMenu.add_command(label='open',command= openclick)
subMenu.add_separator()
subMenu.add_command(label='close',command= close)

subMenu2=Menu(menu,tearoff=0)
menu.add_cascade(label='edit',menu=subMenu2)
subMenu2.add_command(label='undo',command= undo)
subMenu2.add_command(label='redo',command= redo)
subMenu2.add_separator()
subMenu2.add_command(label='cut',command= cut)
subMenu2.add_command(label='copy',command= copy)
subMenu2.add_command(label='paste',command= paste)

root.mainloop()