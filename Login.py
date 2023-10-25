import tkinter as tk
from tkinter import messagebox

# Function to check login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

# Replace this with your own authentication logic
    if username == "Test" and password == "Test123":
        messagebox.showinfo("Login Status", "Login Successful")
    else:
        messagebox.showerror("Login Status", "Login Failed")

# Create the main window
window = tk.Tk()
window.title("Login Page")

# Create labels for username and password
label_username = tk.Label(window, text="Username:")
label_password = tk.Label(window, text="Password:")

# Create entry widgets for user input
entry_username = tk.Entry(window)
entry_password = tk.Entry(window, show="*") # Show '*' for password input

# Create a login button
login_button = tk.Button(window, text="Login", command=login)

# Place widgets on the window using the grid layout
label_username.grid(row=0, column=0)
entry_username.grid(row=0, column=1)
label_password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)
login_button.grid(row=2, columnspan=2)

# Start the Tkinter main loop
window.mainloop()
