import mysql.connector
from tkinter import *

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1305",
  database="student"
)

# Create a cursor object
crsr = mydb.cursor()

# Define a function to handle the login button
def login():
    # Get the entered username and password
    uid = entry1.get()
    password = entry1.get()
    
    # Execute a SELECT query to check if the user exists
    crsr.execute("SELECT * FROM register WHERE id = %s AND password = %s", (uid, password))
    
    # Fetch the results of the query
    result = crsr.fetchone()
    
    # If the query returned a result, the login was successful
    if result:
        print("Login successful")
    else:
        print("Invalid username or password")

# Create the login form
root = Tk()
root.title("Login Form")

# Username label and entry
label1 = Label(root, text="Username:")
label1.grid(row=0, column=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)

# Password label and entry
label2 = Label(root, text="Password:")
label2.grid(row=1, column=0)
entry2 = Entry(root, show="*")
entry2.grid(row=1, column=1)

# Login button
btn = Button(root, text="Login", command=login)
btn.grid(row=2, column=0, columnspan=2)

root.mainloop()
