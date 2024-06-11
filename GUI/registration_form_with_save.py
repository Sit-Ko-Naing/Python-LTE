import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import os

# Function to save information to a text file
def save_info():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    
    if not name or not age or not gender:
        messagebox.showwarning("Incomplete Data", "Please fill in all fields")
        return
    
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Gender: {gender}\n")
        messagebox.showinfo("Success", "Information saved successfully")

# Function to clear the input fields
def clear_info():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set('')

# Create the main window
root = tk.Tk()
root.title("Save Information")

# Create and place the labels, entry boxes, and drop-down menu
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=10)
gender_var = tk.StringVar()
gender_menu = ttk.Combobox(root, textvariable=gender_var)
gender_menu['values'] = ('Male', 'Female', 'Other')
gender_menu.grid(row=2, column=1, padx=10, pady=10)

# Create and place the Submit and Clear buttons
submit_button = tk.Button(root, text="Submit", command=save_info)
submit_button.grid(row=3, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_info)
clear_button.grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
