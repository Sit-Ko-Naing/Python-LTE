import tkinter as tk 
from tkinter import font

def read_from_file():
    path = "text\country_city.txt"
    my_file = open(path,"r")
    lines = my_file.readlines()
    my_dict = {}
    for line in lines:
        line = line.rstrip("\n")
        country,city=line.split("/")
        my_dict[country]=city
    return my_dict

#get input from entry box
def get_capital():
   country = text_box.get()
   capital = my_dict[country]
   capital = (f"The capital city of {country} is {capital}")
   capital_label.config(text=capital )

Window = tk.Tk()
Window.title("Ask the Expert")
Window.configure(bg='#6F99B2')  # Light blue background

# Setting a nice font
custom_font = font.Font(family="Helvetica", size=20)

# Configuring the grid layout for better spacing
Window.columnconfigure(0, weight=1, pad=10)
Window.columnconfigure(1, weight=1, pad=10)
Window.rowconfigure(0, pad=10)
Window.rowconfigure(1, pad=10)


tk.Label(Window, text="Type the name of the country:", font=custom_font, bg='#6F99B2').pack()
text_box = tk.Entry(Window, width=40, font=custom_font, bg='#6F9000')
text_box.pack()
capital_label = tk.Label(Window, font=custom_font, bg='#6F99B2')
capital_label.pack()
my_dict = read_from_file() 
ok_button = tk.Button(Window, text="OK", command=get_capital, font=custom_font, bg='#6F99B2').pack()

Window.mainloop()