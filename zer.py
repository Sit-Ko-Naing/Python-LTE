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