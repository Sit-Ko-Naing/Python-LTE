from tkinter import *
from PIL import Image,ImageTk
from datetime import date

root = Tk()
root.geometry("500x300")
root.title("Age Calculator")
root.config(bg="pink")

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    # age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    age = today.year - birthDate.year
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6, column=1)

    if age<2:
        Label(text="You are just a baby!", font=('Arial', 15), relief=SOLID, bg='blue').grid(row=6, column=0, padx=90)

    if age<=10:
        Label(text="You are still an underage!", font=('Arial', 15), relief=SOLID, bg='blue').grid(row=6, column=0, padx=90)
    if age<20:
        Label(text="You are a teenager", font=('Arial', 15), relief=SOLID, bg='blue').grid(row=6, column=0, padx=90)
    if age>=20:
        Label(text="You are an adult!", font=('Arial', 15), relief=SOLID, bg='blue').grid(row=6, column=0, padx=90)


    
Label(text="Name").grid(row=1, column=0, padx=90)
Label(text="Year").grid(row=2, column=0)
Label(text="Month").grid(row=3, column=0)
Label(text="Day").grid(row=4, column=0)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)

nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

computeButton = Button(text="CalculateAge", command=calculateAge)
computeButton.grid(row=5, column=1, pady=10)
root.mainloop()