from tkinter import Tk, Canvas, Button
window = Tk()
window.title("Example GUI")
c = Canvas(window, width=800, height=600, bg='black')
c.pack()
c.create_text(50, 50, anchor='w', fill='orange', font='Arial 28 bold underline',\
             text="What you'll learn in Level-2")

def get_outline(filename):
    list_outline= []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            list_outline.append(line)
    return list_outline


def display_outline(outlines):

    vertical_space = 200
    count = 1 
    for outline in outlines :
        c.create_text(50, vertical_space, anchor='w', fill='lightblue', \
                    font='Arial 28 bold', text= str(count) + ". " + outline)
        vertical_space = vertical_space + 30
        count += 1

    c.create_text(50, vertical_space + 30, anchor='w', fill='orange', \
                font='Arial 28 bold', text= "See you in Level-2 !")

def clicked():
    outlines = get_outline("outline.txt")
    display_outline(outlines)

btn = Button(window, text="Let's Check Out!", command=clicked)
btn.place(x=300, y=100)

window.mainloop()