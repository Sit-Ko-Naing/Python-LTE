
import tkinter as tk
from tkinter import PhotoImage
import webbrowser
from PIL import Image, ImageTk

def open_link():
    webbrowser.open("https://github.com/Sit-Ko-Naing/Python-LTE/")

# Create the main window
root = tk.Tk()
root.title("Link Button Example")

# Load the image
myBaby= Image.open("C:\\Users\\Huawei Matebook 15\\OneDrive\\Desktop\\3000.jpg")
resized_image= myBaby.resize((300,300))
img= ImageTk.PhotoImage(resized_image)

# Create a button that acts as a link with an image
link_button = tk.Button(root, text="Python Lesson", image=img, compound=tk.LEFT, fg="blue", cursor="hand2", command=open_link)
link_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
