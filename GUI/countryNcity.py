import tkinter as tk
from tkinter import font

#output of countryNcity text file to dict file
def read_from_file():
   path = "text\countryNcity.txt"
   my_file = open(path,"r")
   lines = my_file.readlines()
   my_dict = {}
   for line in lines:
       line = line.rstrip("\n")
       country,city = line.split("/")
       my_dict[country] = city
   return my_dict

#get input from entry box
def get_capital():
   country = text_box.get()
   capital = my_dict[country]
   capital = (f"The capital city of {country} is {capital}")
   capital_label.config(text=capital )


# Create the main window
window = tk.Tk()
window.title("Ask the Expert")
window.configure(bg='#6F99B2')  # Light blue background

# Setting a nice font
custom_font = font.Font(family="Helvetica", size=14)

# Configuring the grid layout for better spacing
window.columnconfigure(0, weight=1, pad=10)
window.columnconfigure(1, weight=1, pad=10)
window.rowconfigure(0, pad=10)
window.rowconfigure(1, pad=10)

tk.Label(window, text = "Type the name of a country:", font=custom_font, bg='#6F99B2').pack()
text_box = tk.Entry(window, width = 50, font=custom_font, bg='#0009B2')
text_box.pack()
capital_label = tk.Label(window, font=custom_font, bg='#6F99B2')
capital_label.pack()
my_dict = read_from_file() 
ok_button = tk.Button(window, text = "OK", command = get_capital, font=custom_font, bg='#6F99B2' )
ok_button.pack()

window.mainloop()
