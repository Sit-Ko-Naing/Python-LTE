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