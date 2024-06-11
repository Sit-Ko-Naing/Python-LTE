from tkinter import *
import random

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x300')
ws.config(bg='#4a7a8c')

ranNum = random.randint(0, 5)
print(ranNum)
chance = 5
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'You won! {ranNum} is the right answer.'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempt left.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)


Label(
    ws,
    text='Number Guessing Game',
    font=('Arial', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='pink'
).place(x=100,y=20)

Entry(
    ws,
    textvariable=var,
    font=('Arial', 18)
).place(x=130,y=100)

Button(
    ws,
    text='Submit Guess',
    font=('Arial', 18),
    command=check_guess
).place(x=160, y=150)

Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    font=('Arial', 14)
).place(x=100,y=220)


ws.mainloop()