from tkinter import *  
from PIL import ImageTk,Image  

def resize_func():
    image = Image.open("images\\f22.jpg")
    w = int(width.get())
    h = int(height.get())
    resize_img = image.resize((w, h))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img

ws = Tk()
ws.title('Image resize')
ws.geometry('500x500')
ws.config(bg='#FFE873')

# Label widget and Entry widget for width
Label(ws, text='Width', width=8).place(x=0, y=0)
width = Entry(ws, width=10)
width.insert(END, 300)
width.place(x=80, y=0)

# for height
Label(ws, text='Height', width=8).place(x=0 ,y=20)
height = Entry(ws, width=10)
height.insert(END, 350)
height.place(x=80, y=20)

# Button for resize
resize_btn = Button(ws, text='Resize', command=resize_func)
resize_btn.place(x=50, y=50)

# Image display label
disp_img = Label(ws)
disp_img.place(x=80, y=80)


ws.mainloop()