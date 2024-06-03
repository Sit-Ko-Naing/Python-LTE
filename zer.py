#Temperature Converter

import tkinter as tk

def celcius_to_fahrenheit():
    celcius = float(entry_celcius.get())
    fahrenheit = ( celcius * 9/5) + 32
    my_label2.config(text=f'{fahrenheit} °F')


root = tk.Tk()
root.title("Temperature Converter")

my_label = tk.Label(root, text="Celcius")
my_label.grid(row=0,column=0)

my_label2 = tk.Label(root, text="")
my_label2.grid(row=1,column=1)

entry_celcius = tk.Entry(root, width=20)
entry_celcius.grid(row=0,column=1)

my_button = tk.Button(root, text="Convert", command=celcius_to_fahrenheit)
my_button.grid(row=1, column=0)

root.mainloop()