import tkinter as tk

def greet():
    name = "Hello guys, " + my_text_box.get()
    name_lable.config(text=name)

window = tk.Tk()
window.title("Greeting")

my_lable = tk.Label(window, text="Enter your name : ")
my_lable.grid(row=0, column=0)

name_lable = tk.Label(window, text="text lable ")
name_lable.grid(row=1, column=0)

my_text_box = tk.Entry(window, width=20)
my_text_box.grid(row=0,column=1)

my_button = tk.Button(window, text="Hello!", command=greet)
my_button.grid(row=1, column=1)

window.mainloop()

# _______________________________________________________________________

# Empty window

import tkinter as tk


def greet():
    name = "Hello " + my_text_box.get()
    my_lab.config(text=name)

def hi():
    name2 = "Hi" + my_text_box2.get()
    my_lab2.config(text=name2)


root = tk.Tk()
root.title("Hello")

my_lab = tk.Label(root, text= "Enter your name : ") #Label
my_lab.grid(row=0,column=0)

my_lab2 = tk.Label(root, text= "Enter your age : ")
my_lab2.grid(row=1,column=0)

my_text_box = tk.Entry(root, width=40)
my_text_box.grid(row=0,column=1)

my_text_box2 = tk.Entry(root, width=40)
my_text_box2.grid(row=1,column=1)

my_button = tk.Button(root, text="Click1", command=greet)
my_button.grid(row=2,column=0)

my_button2 = tk.Button(root, text="Click2", command=hi)
my_button2.grid(row=2,column=1)

root.mainloop()