# #Add Drop Down Menu

# import tkinter as tk
# from tkinter import IntVar, OptionMenu

# # Create the main window
# window = tk.Tk()
# window.title("Dropdown Menu Example")

# # Define the options for the dropdown
# options = (1, 2, 3)
# options1 = (2,3,4)

# # Create a variable to store the selected option
# menu = IntVar()
# menu.set("choose:")

# # Create the dropdown menu
# my_dropdown = OptionMenu(window, menu, *options)
# my_dropdown.grid(row=1, column=1, padx=10, pady=10)

# # Create the dropdown menu
# my_dropdown1 = OptionMenu(window, menu, *options1)
# my_dropdown1.grid(row=0, column=1, padx=10, pady=10)


# # Run the Tkinter event loop
# window.mainloop()

# _______________________________________________________________________________________

# #Add An image
# from tkinter import *
# from PIL import Image, ImageTk

# # Create the main window
# window = Tk()
# window.title("Image Example")
# window.geometry("300x300")

# # Load the image using Pillow
# myBaby= Image.open("images\\f22.jpg")
# resized_image= myBaby.resize((300,300))
# img= ImageTk.PhotoImage(resized_image)

# # Create a label to display the image
# img_label = Label(window, image=img)
# img_label.grid(row=0, column=0)

# # Keep a reference to the image to prevent it from being garbage collected
# img_label.image = img

# # Run the Tkinter event loop
# window.mainloop()

# _____________________________________________________________________________________________

#Link Button

# import tkinter as tk
# import webbrowser

# def open_link():
#     webbrowser.open("https://www.youtube.com/watch?v=mNrzmpA8JU4")

# # Create the main window
# root = tk.Tk()
# root.title("Link Button Example")

# # Create a button that acts as a link
# link_button = tk.Button(root, text="Open Example.com", fg="blue", cursor="hand2", command=open_link)
# link_button.pack(pady=20)

# # Run the Tkinter event loop
# root.mainloop()

# ____________________________________________________________________________________

import tkinter as tk
from tkinter import PhotoImage
import webbrowser
from PIL import Image, ImageTk

def open_link():
    webbrowser.open("https://www.youtube.com/watch?v=mNrzmpA8JU4")

# Create the main window
root = tk.Tk()
root.title("Link Button Example")

# Load the image
myBaby= Image.open("images\\f22.jpg")
resized_image= myBaby.resize((300,300))
img= ImageTk.PhotoImage(resized_image)

# Create a button that acts as a link with an image
link_button = tk.Button(root, text="Open Example.com", image=img, compound=tk.LEFT, fg="blue", cursor="hand2", command=open_link)
link_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
