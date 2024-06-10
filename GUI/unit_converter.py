import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to handle length conversion
def convert_units():
    try:
        value = float(input_entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()
        
        if from_unit == 'cm' and to_unit == 'm':
            converted_value = value / 100
        elif from_unit == 'm' and to_unit == 'cm':
            converted_value = value * 100
        elif from_unit == 'kg' and to_unit == 'pounds':
            converted_value = value * 2.20462
        elif from_unit == 'pounds' and to_unit == 'kg':
            converted_value = value / 2.20462
        elif from_unit == to_unit:
            converted_value = value
        else:
            raise ValueError("Incompatible units for conversion.")
        
        output_var.set(f"{converted_value:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.configure(bg="pink")

# Input section
tk.Label(root, text="Input", bg="pink").grid(row=0, column=0, columnspan=2, pady=10)

input_entry = tk.Entry(root, width=15)
input_entry.grid(row=1, column=0, padx=10, pady=5)

from_var = tk.StringVar(value='m')
from_menu = ttk.Combobox(root, textvariable=from_var, values=('cm', 'm', 'kg', 'pounds'), width=5)
from_menu.grid(row=1, column=1, padx=10, pady=5)

# Output section
tk.Label(root, text="Output", bg="pink").grid(row=2, column=0, columnspan=2, pady=10)

output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var, state='readonly', width=15)
output_entry.grid(row=3, column=0, padx=10, pady=5)

to_var = tk.StringVar(value='cm')
to_menu = ttk.Combobox(root, textvariable=to_var, values=('cm', 'm', 'kg', 'pounds'), width=5)
to_menu.grid(row=3, column=1, padx=10, pady=5)

# Convert button
convert_button = tk.Button(root, text="OK", command=convert_units, bg="white")
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
