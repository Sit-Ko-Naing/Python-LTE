# Error , need to fix

import random
import tkinter as tk
window = tk.Tk()
window.title("My8Ball")

answers = (
    "Most likely",
    "Very doubtful",
    "I'm not sure. Ask me again.",
    "As I see it, yes.",
    "My sources say no.",
    "Cannot predict now.",
    "Makes no difference to me, do or don't - whatever.",
    "Yes, I think on balance that is the right choice."
    )
def shake_ball():
    choice=random.randint(0, 7)
    advice.config(text=answers[choice])

def greet():
    name = "Hello," + my_text_box.get() +"."
    name_label.config(text=name + " Welcome to My8ball.")
  
my_label = tk.Label(window, text="Enter your name:")
my_label.pack()

my_text_box = tk.Entry(window, width=50) 
my_text_box.pack()
my_button = tk.Button(window, text="Start", command=greet) 
my_button.pack()
name_label = tk.Label(window, text = " ")
name_label.pack()

tk.Label(window, text="Ask me for advice then press SHAKE.").pack()
question = tk.Entry(window,width = 50)
question.pack()
ball = tk.PhotoImage(file="C:\\Users\\Huawei Matebook 15\\OneDrive\\Desktop\\Python-LTE\\images\\f22.jpg")
tk.Label(window, image=ball).pack()
shake = tk.Button(window, text="SHAKE", command = shake_ball)
shake.pack()
advice = tk.Label(window,text =" ")
advice.pack()

window.mainloop()