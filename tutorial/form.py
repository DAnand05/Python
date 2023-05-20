# create a registration form using tkinter
import tkinter as tk
import tkinter as messagebox
# Create a new tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Registration Form")

# Create the labels for each input field
label1 = tk.Label(window, text="Name:")
label2 = tk.Label(window, text="Email:")
label3 = tk.Label(window, text="Password:")

# Create the entry fields for each input
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window, show="*")

# Place the labels and entry fields in the window using a grid layout
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)

# Define a function to be called when the submit button is pressed
def submit():
    # Get the values from the entry fields
    name = entry1.get()
    email = entry2.get()
    password = entry3.get()
    
    # Print the values to the console
    print("Name:", name ,"\nEmail:", email ,"\nPassword:", password)
    messagebox.showinfo("Alert","name:"+name,"password:"+password)
# Create the submit button
btn = tk.Button(window, text="Submit", command=submit)

# Place the submit button in the window using a grid layout
btn.grid(row=3, column=1)

# Start the tkinter event loop
window.mainloop()
