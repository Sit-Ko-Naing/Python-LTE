from tkinter import *

# Conversion factors
unit_dict = {
    "cm" : 0.01,
    "m" : 1.0,
    "km": 1000.0,
    "kg" : 1000.0,
    "pounds" : 453.592
}

lengths = ["cm", "m", "km"]
weights = ["kg", "pounds",]

# Options for drop-down menu
OPTIONS = ["cm",
            "m",
            "km",
            "kg",
            "pounds"]

# Main window
root = Tk()
root.geometry("400x350")
root.title("Unit Converter")
root['bg'] = 'pink'

def ok():
    inp = float(inputentry.get())
    inp_unit = inputopt.get()
    out_unit = outputopt.get()

    cons = [inp_unit in lengths and out_unit in lengths,
    inp_unit in weights and out_unit in weights]

    if cons[0] or cons[1]:
        outputlabel.config(text=round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))
    else: # Display error if units are of different types
        outputlabel.config(text="ERROR")

inputopt = StringVar()
inputopt.set("Select unit:")

outputopt = StringVar()
outputopt.set("Select unit:")

# Widgets
inputlabel = Label(root, text = "Input")
inputlabel.grid(row = 0, column = 0, pady = 20)

inputentry = Entry(root, justify = "center", font = "bold")
inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

inputmenu = OptionMenu(root, inputopt, *OPTIONS)
inputmenu.grid(row = 1, column = 1)
inputmenu.config(font = "Arial 10")

outputlabel = Label(root, text = "Output")
outputlabel.grid(row = 2, column = 0, pady = 20)

outputlabel = Label(root, justify = "center", font = "bold")
outputlabel.grid(row = 3, column = 0, padx = 35, ipady = 5)

outputmenu = OptionMenu(root, outputopt, *OPTIONS)
outputmenu.grid(row = 3, column = 1)
outputmenu.config(font = "Arial 10")

okbtn = Button(root, text = "OK", command = ok, padx = 80, pady = 2)
okbtn.grid(row = 4, column = 0, columnspan = 2, pady = 50)

root.mainloop()