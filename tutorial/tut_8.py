import tkinter as tk
import sqlite3

# Create a connection to the database
db = sqlite3.connect("student.db")
cursor = db.cursor()

def insert_data():
    # Get the data from the entry fields
    id = int(entry1.get())
    name = entry2.get()
    branch = entry3.get()
    address = entry4.get()
    course = entry5.get()

    # Insert the data into the register table
    cursor.execute(f"INSERT INTO register (id, name, branch, address, course) VALUES ({id}, '{name}', '{branch}', '{address}', '{course}')")
    db.commit()

    # Clear the entry fields
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)

def delete_data():
    # Get the ID to delete
    id = int(entry1.get())

    # Delete the row from the register table
    cursor.execute(f"DELETE FROM register WHERE id = {id}")
    db.commit()

    # Clear the entry field
    entry1.delete(0, tk.END)

mainscreen = tk.Tk()
mainscreen.geometry("400x300")  # Set the size of the frame

label1 = tk.Label(mainscreen, text="Your ID")
label2 = tk.Label(mainscreen, text="Your name")
label3 = tk.Label(mainscreen, text="Your branch")
label4 = tk.Label(mainscreen, text="Your address")
label5 = tk.Label(mainscreen, text="Your course")
label1.place(x=10, y=10)
label2.place(x=10, y=50)
label3.place(x=10, y=90)
label4.place(x=10, y=130)
label5.place(x=10, y=170)

entry1 = tk.Entry(mainscreen, bd=1)
entry2 = tk.Entry(mainscreen, bd=1)
entry3 = tk.Entry(mainscreen, bd=1)
entry4 = tk.Entry(mainscreen, bd=1)
entry5 = tk.Entry(mainscreen, bd=1)
entry1.place(x=120, y=10)
entry2.place(x=120, y=50)
entry3.place(x=120, y=90)
entry4.place(x=120, y=130)
entry5.place(x=120, y=170)

insert_btn = tk.Button(mainscreen, text="Insert", command=insert_data)
insert_btn.place(x=120, y=210)

delete_btn = tk.Button(mainscreen, text="Delete", command=delete_data)
delete_btn.place(x=200, y=210)

mainscreen.mainloop()

# Close the cursor and database connection
cursor.close()
db.close()
