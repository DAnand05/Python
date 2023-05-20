import tkinter as tk
import smtplib
import sqlite3

db=sqlite3.connect("email.db")
cursor=db.cursor()

cursor.execute('''Create table IF NOT EXISTS logs(
id integer primary Key autoincrement,
reciepient text,
subject text,
message text
)''')

def SendMail():
    recipient=entry1.get()
    subject=entry2.get()
    message=textBox.get("1.0",tk.END)

    cursor.execute(f"INSERT INTO register (id, recipient, subject, message) VALUES (, '{recipient}', '{subject}', '{message}')")

    db.commit()

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    textBox.delete(1.0, tk.END)

mainscreen=tk.Tk()

label1=tk.Label(mainscreen,text="Recipient: ")
label2=tk.Label(mainscreen,text="Subject: ")
label3=tk.Label(mainscreen,text="Message: ")

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)

entry1=tk.Entry(mainscreen, width=30)
entry2=tk.Entry(mainscreen, width=30)
textBox=tk.Text(mainscreen, width=30, height=10)

entry1.grid(row=0,column=1,padx=5,pady=5)
entry2.grid(row=1,column=1,padx=5,pady=5)
textBox.grid(row=2,column=1,padx=5,pady=5)

btn=tk.Button(mainscreen,text="Send",command="SendMail")
btn.grid(row=3,column=1,pady=10)

mainscreen.mainloop()

cursor.close()
db.close()
