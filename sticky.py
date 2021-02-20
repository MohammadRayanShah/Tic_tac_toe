from tkinter import *
root= Tk()
label1=Label(root,text='Label1',bg='red')
label1.grid(row='0',column='0',ipadx='150',ipady='150')

label2=Label(root,text='Label2',bg='silver')
label2.grid(row='0',column='1',sticky=W)

label3=Label(root,text='Label3',bg='blue')
label3.grid(row='1',column='0',sticky=N+S)

label4=Label(root,text='Label4',bg='orange')
label4.grid(row='1',column='1',ipadx='150',ipady='150')
root.mainloop()