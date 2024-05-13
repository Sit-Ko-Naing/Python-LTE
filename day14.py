# Function 

# Built-in Function -----  User-defined function

# void function  -------  type function

#dynamic type function === def function-name()

def greeting():
    print("THis is greeting function.")

print("hello, world.")
greeting()

# ___________________________________________________________________________________

def addition():
    print("this is 4 + 5 addition function ")
    a  = 4
    b = 5
    return a+b  #return ရဲ့ အနောက်က code တွေကို ဆက်အလုပ်မလုပ်ပါ။

result = addition()

print(result)

# ____________________________________________________________________________________

def func():
    print("Statemaent from function")


print("Normal Statement 1")
print("Normal Statement 2")
func()
print("Normal Statement 3")

# _______________________________________________________________________________________

#parameter / argument

#def function-name(parameter)

#function-name(argument)


def add():
    a = 4
    b = 5
    return a+b

total = add()
print(total)

# ______________________________________________________________________________________

def add(num1,num2):
    return num1 + num2

result = add(3,4)
print(result)

# ______________________________________________________________________________________

def add(n1,n2):
    n3 = n1 + 1
    n4 = n2 + 1
    return n3 + n4

def sub(n1,n2):
    return n1 - n2

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
opt = input("addition for A | subtraction for S : ")

if opt == "A":
    result = add(num1,num2)
elif opt == "S":
    result = sub(num1,num2)
else:
    print("Try again.")


print(f"Total result : {result}")

# __________________________________________________________________________________