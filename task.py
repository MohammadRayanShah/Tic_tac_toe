from tkinter import *
def click():
    temp = entry.get()

    value.set(temp + 'x' + '1 = ' +  temp)

    two = int(temp) * 2
    value2.set(temp + 'x' + ' 2 = ' + str(two) )

    three=int(temp)*3
    value3.set(temp + 'x' + '3 = ' + str(three))

    four=int(temp)*4
    value4.set(temp + 'x' + '4 = ' + str(four))

    five=int(temp)*5
    value5.set(temp + 'x' + '5 = ' + str(five))

    six=int(temp)*6
    value6.set(temp + 'x' + '6 = ' + str(six))

    seven=int(temp)*7
    value7.set(temp + 'x' + '7 = ' + str(seven))

    eight=int(temp)*8
    value8.set(temp + 'x' + '8 = ' + str(eight))

    nine=int(temp)*9
    value9.set(temp + 'x' + '9 = ' + str(nine))

    ten=int(temp)*10
    value10.set(temp + 'x' + '10 = ' + str(ten))
root = Tk()

entry = Entry(root)
entry.pack()

Button(root,text='click here',command=click).pack()
value=IntVar()
value.set('-----')
label=Label(root, textvar= value,bg ='red')
label.pack()

value2=IntVar()
value2.set('-----')
label=Label(root, textvar= value2,bg ='red')
label.pack()

value3=IntVar()
value3.set('-----')
label=Label(root, textvar= value3,bg ='red')
label.pack()

value4=IntVar()
value4.set('-----')
label=Label(root, textvar= value4,bg ='red')
label.pack()

value5=IntVar()
value5.set('-----')
label=Label(root, textvar= value5,bg ='red')
label.pack()

value6=IntVar()
value6.set('-----')
label=Label(root, textvar= value6,bg ='red')
label.pack()

value7=IntVar()
value7.set('-----')
label=Label(root, textvar= value7,bg ='red')
label.pack()

value8=IntVar()
value8.set('-----')
label=Label(root, textvar= value8,bg ='red')
label.pack()

value9=IntVar()
value9.set('-----')
label=Label(root, textvar= value9,bg ='red')
label.pack()

value10=IntVar()
value10.set('-----')
label=Label(root, textvar= value10,bg ='red')
label.pack()

root.mainloop()