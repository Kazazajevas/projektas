from tkinter import*
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
box=tk.Tk()
box.title('Vr Bardakas')

#box.tk.call('wm', 'iconphoto', box._w, tk.PhotoImage(file='Untitled-1.jpg'))
username=[]

answer = simpledialog.askstring("Login", "Please write your username",
parent=box)
if answer is not None:
 username.append(answer)
else:
 messagebox.showerror("Error","Please try again")


def send():
    f = open('serveris.txt', 'a+')
    a=x.get()
    y.config(text=a)
    f.write(a)
    f.close()
    x.delete(0,END)
def smile():
    a=x.get()
    x.delete(0,END)
    x.insert(0,str(a)+str(":)"))
def sad():
    x.delete(0, END)
    x.insert(0, ":(")

x=Entry(box,width=100,borderwidth=10,bg="#2E1A47",)
x.grid(row=5, column=0,columnspan=5,pady=10)
#x.place()
y=Label(box,text="",width=100,height=25,borderwidth=5,bg="#6c9fce")
y.grid(row=0,column=0,rowspan=4)
#y.place()
x.insert(0,"")

bttnsend=Button(box,width=10,text="Send",command=send)
bttnsend.grid(row=5,column=3,)
#bttnsend.place()
smile=Button(box,width=5,text=":)",command=lambda:smile)
smile.grid(row=4,column=0)
#smile.place()
sad=Button(box,width=10,text=":(",command=lambda:sad)
sad.grid(row=4,column=1)
#sad.place()
box.mainloop()