import tkinter as tk
window = tk.Tk()
window.title("Registration Form")

def writeFile():
    file = open("course_register.txt","a")
    n = name.get()
    file.write(n + "/")
    e= email.get()
    file.write(e + "/")
    file.write(age.get() + "/")
    file.write(g.get() + "/")
    file.write(contact.get() + "/")
    file.write(c.get() + "\n")
    file.close()

def clear():
    name.delete(0, tk.END)
    age.delete(0, tk.END)
    email.delete(0, tk.END)
    contact.delete(0, tk.END)
    g.set("Choose:")
    c.set("Choose:")

tk.Label(window, text="Course Registration Form").grid(row = 0, column = 0)

nlabel = tk.Label(window, text="Name:")
nlabel.grid(row=1, column= 0)
name = tk.Entry(window, width = 20)
name.grid(row = 1, column =1)

elabel = tk.Label(window, text="Email:")
elabel.grid(row=2, column= 0)
email = tk.Entry(window, width = 20)
email.grid(row = 2, column =1)

alabel = tk.Label(window, text="Age")
alabel.grid(row=3, column= 0)
age = tk.Entry(window, width = 20)
age.grid(row = 3, column =1)

glabel = tk.Label(window, text="Gender:")
glabel.grid(row=4, column= 0)
options = ("Male","Female","Others")
g = tk.StringVar()
g.set("Choose:")
gender = tk.OptionMenu(window, g, *options) 
gender.grid(row=4, column= 1)

clabel = tk.Label(window, text="Contact number:")
clabel.grid(row=5, column= 0)
contact = tk.Entry(window, width = 20)
contact.grid(row = 5, column =1)

course_label = tk.Label(window, text="Select course:")
course_label.grid(row=6, column= 0)
options = ("PY4Y","AI4Y", "3D4Y","Arduino","English")
c = tk.StringVar()
c.set("Choose:")
course = tk.OptionMenu(window, c, *options) 
course.grid(row = 6, column =1)

submit = tk.Button(window, text="Submit", command = writeFile)
submit.grid(row = 7,column = 0)

clear_b = tk.Button(window, text="Clear", command = clear)
clear_b.grid(row = 7,column = 1)

window.mainloop()