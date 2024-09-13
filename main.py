from tkinter import *
from tkinter import messagebox
root=Tk()
root.title=('Virus detector')
root.geometry=('300x300')

def msg():
    messagebox.showwarning('Virus detected',"Stay alert")
b1=Button(root,text='Scan Virus',command=msg)
b1.pack()
root.mainloop()