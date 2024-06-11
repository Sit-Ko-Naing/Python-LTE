import tkinter as tk
from tkinter import font

# def celsius_to_fahrenheit():
#     celsius = float(entry_celsius.get())
#     fahrenheit = (celsius * 9/5) + 32
#     label_result.config(text=f'{fahrenheit:.2f} °F',bg='#add8e6')

#Addition Function

def addition():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    total = num1 + num2
    # label_result.config(text=f'{total} °F',bg='#add8e6')
    label_result.config(text=f"Total : {total}",bg='#add8e6')


def subtraction():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    total = num1 - num2
    # label_result.config(text=f'{total} °F',bg='#add8e6')
    label_result.config(text=f"Total : {total}",bg='#add8e6')


root = tk.Tk()
root.title("Temperature Converter")
root.configure(bg='#bbbbcc')  # Light blue background

# Setting a nice font
custom_font = font.Font(family="Helvetica", size=14)

# Configuring the grid layout for better spacing
root.columnconfigure(0, weight=1, pad=10)
root.columnconfigure(1, weight=1, pad=10)
root.rowconfigure(0, pad=10)
root.rowconfigure(1, pad=10)

first_num = tk.Entry(root, width=20, font=custom_font, bg='#f0f8ff')
first_num.grid(row=0, column=1, padx=10, pady=10)

sec_num = tk.Entry(root, width=20, font=custom_font, bg='#f0f8ff')
sec_num.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Enter Num : ", font=custom_font, bg='#ffaaff').grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="+",font=custom_font, bg='#87cefa', fg='black', command=addition).grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="-",font=custom_font, bg='#87cefa', fg='black', command=subtraction).grid(row=2, column=0, padx=10, pady=10)



label_result = tk.Label(root, text="Result", font=custom_font, bg='#f0f8ff')
label_result.grid(row=1, column=2, pady=10)

root.mainloop()
