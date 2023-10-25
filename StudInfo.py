import tkinter as tk
def save_student_info():
    # Get data from input fields and save to a database or file
    name = entry_name.get()
    roll_number = entry_roll.get()

    # Add data processing logic here
    print(f"Saved Student: {name}, Roll: {roll_number}")
    
# Create the main window
window = tk.Tk()
window.title("Student Information Form")
    
# Create labels and entry widgets for student data
label_name = tk.Label(window, text="Name:")
label_roll = tk.Label(window, text="Roll Number:")
entry_name = tk.Entry(window)
entry_roll = tk.Entry(window)
save_button = tk.Button(window, text="Save", command=save_student_info)

# Place widgets on the window using the grid layout
label_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
label_roll.grid(row=1, column=0)
entry_roll.grid(row=1, column=1)
save_button.grid(row=2, columnspan=2)
window.mainloop()