import tkinter as tk
import smtplib
import sqlite3

# Create a connection to the database
db = sqlite3.connect("email_logs.db")
cursor = db.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS email_logs
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   recipient TEXT,
                   subject TEXT,
                   message TEXT)''')

def send_email():
    # Get the data from the entry fields
    recipient = entry1.get()
    subject = entry2.get()
    message = text_box.get("1.0", tk.END)

    # Configure the SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Create the SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email message
        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(smtp_username, recipient, email_message)

    # Log the email in the database
    cursor.execute("INSERT INTO email_logs (recipient, subject, message) VALUES (?, ?, ?)",
                   (recipient, subject, message))
    db.commit()

    # Clear the entry fields and text box
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    text_box.delete("1.0", tk.END)

# Create the main window
mainscreen = tk.Tk()

# Create and place the labels
label1 = tk.Label(mainscreen, text="Recipient:")
label2 = tk.Label(mainscreen, text="Subject:")
label3 = tk.Label(mainscreen, text="Message:")

label1.grid(row=0, column=0, sticky="e")
label2.grid(row=1, column=0, sticky="e")
label3.grid(row=2, column=0, sticky="nw")

# Create and place the entry fields
entry1 = tk.Entry(mainscreen, width=30)
entry2 = tk.Entry(mainscreen, width=30)

entry1.grid(row=0, column=1, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Create and place the text box
text_box = tk.Text(mainscreen, width=30, height=10)
text_box.grid(row=2, column=1, padx=5, pady=5)

# Create and place the send button
send_btn = tk.Button(mainscreen, text="Send", command=send_email)
send_btn.grid(row=3, column=1, pady=10)

# Start the GUI main loop
mainscreen.mainloop()

# Close the database connection
cursor.close()
db.close()
