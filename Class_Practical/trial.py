import tkinter as tk
from tkinter import messagebox

mainscreen = tk.Tk()
mainscreen.geometry("300x200")

var=tk.IntVar()

label=tk.Label(mainscreen,text="Death Note")
label.place(x=10,y=10)
chkbtn1=tk.Checkbutton(mainscreen,text="first")
chkbtn2=tk.Checkbutton(mainscreen,text="second")
val1=tk.IntVar();
val2=tk.IntVar();
tk.getval():
lang="
ing1=var1.get()
ing2=var2.get()"
btn = tk.Button(mainscreen, text="Hello",background='cyan',foreground='magenta',width=20,height=2,activebackground='Yellow',activeforeground='red')

btn.place(x=50,y=100)

entry=tk.Entry(mainscreen,bd=10)
chkbtn1.place(x=50,y=50)
chkbtn2.place(x=150,y=50)
entry.place(x=100,y=10)
mainscreen.mainloop()