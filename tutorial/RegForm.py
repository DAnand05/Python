#create a registration form using tkinter and then print the input data

import tkinter as tk

# Create a new tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Registration Form")

# Create the labels for each input field
label_name = tk.Label(window, text="Name:")
label_email = tk.Label(window, text="Email:")
label_password = tk.Label(window, text="Password:")

# Create the entry fields for each input
entry_name = tk.Entry(window)
entry_email = tk.Entry(window)
entry_password = tk.Entry(window, show="*")

# Place the labels and entry fields in the window using a grid layout
label_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
label_email.grid(row=1, column=0)
entry_email.grid(row=1, column=1)
label_password.grid(row=2, column=0)
entry_password.grid(row=2, column=1)

# Define a function to be called when the submit button is pressed
def submit():
    # Get the values from the entry fields
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    
    # Print the values to the console
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit)

# Place the submit button in the window using a grid layout
submit_button.grid(row=3, column=1)

# Start the tkinter event loop
window.mainloop()
