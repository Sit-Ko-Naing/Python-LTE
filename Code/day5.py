num1 = 10

# num1 = num1 + 3 #increment 
num1 += 3

# num1 = num1 - 3 #decrement
num1 -= 3

print(num1)
# -----------------------------------------------------------------------------------------

apple = 10
melon = 15
berries = 20
potato = 2

pumpkin = berries - apple # 10

apple += 2 # 12
melon -= 3 #12

# pumpkin = berries - apple # 8  

cost = apple + melon + (berries * 2) + pumpkin + potato
print(cost)

# ----------------------------------------------------------------------------------

#PEMDAS

num1 = (2+3)/ 2**3 + (4-2)-(3+1)

# --------------------------------------------------------------------------------------

name = str(input("What is your name :"))
age = int(input("your age : "))

print(f"My name is {name} and {age} years old.")

# ------------------------------------------------------------------------------------------

num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))

total = num1 + num2

print(f"Total result : {total}")

# ------------------------------------------------------------------------------------------

#Boolean Operator

# and or not 

#AND
print((5==5) and (7==7)) #True
print((5==6) and (7==7)) #False
print((5==4) and (7==8)) #False 
#e.g ==> login form 

#OR
print((5==5) or (7==7)) #True
print((5==6) or (7==7)) #True
print((5==4) or (7==8)) #False

# e.g ==> discount

#NOT

print(not 5==4)
print(not 5==5)

# -----------------------------------------------------------------------------------------------

a = 20
b = 10

# print(a>b) #True
# print(a<b) #False
# print( a>b and b == 10) #True
# print( a>b or a == 10 ) #True

# print(a <= 20 and b >= 10) #True
print(not a>= 20) #False
print(not b<9) #True

# ------------------------------------------------------------------------------------
# Conditional Operator

num1 = int(input("Enter a number :"))

if num1 % 2 == 0:
    print(f"{num1} is even number.")
else :
    print(f"{num1} is odd number.")

# ----------------------------------------------------------------------------------------------------


