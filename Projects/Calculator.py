from tkinter import *

def btnClick(numbers):
    global opt
    opt =opt+str(numbers)
    text_Input.set(opt)

def btnClearDisplay():
    global opt
    opt=""
    text_Input.set("")

def equalsum():
    global opt
    sums=str(eval(opt))
    text_Input.set(sums)
    opt=sums

cal=Tk()
cal.title("calculator")
opt="9"
text_Input=StringVar()
txtDisplay=Entry(cal,font=('ariel',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
add=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",command=lambda:btnClick('+')).grid(row=1,column=3)

btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
subb=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",command=lambda:btnClick('-')).grid(row=2,column=3)

btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
mull=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",command=lambda:btnClick('*')).grid(row=3,column=3)

clear=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",command=btnClearDisplay).grid(row=4,column=0)
btn0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",command=lambda:btnClick(0)).grid(row=4,column=1)
equal=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",command=equalsum).grid(row=4,column=2)
divv=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",command=lambda:btnClick('/')).grid(row=4,column=3)

cal.mainloop()