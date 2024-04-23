# for box_counter in range(3):
#    print("Get box!")
#    for cake_counter in range(2):
#        print("Put cake!")

# -------------------------------------------------------------------

# for house in range (1,5):
#    print("House:",house)
#    for year in range (1,8):
#        print("Year:",year)
#        for student in range(10):
#            print("Is this student the best?")

# ----------------------------------------------------------------------

# for i in range(1,4):
#    for j in range(1,4):
#        print(i*j, end ="  ")
#    print()

# ----------------------------------------------------------------------

# for i in range(1,6):
#    for j in range(1,6):
#        print(i*j, end =" ")
#    print()

# -----------------------------------------------------------------------

import random
 
scale = random.random() * 10
scale2 = random.randint(0,100)

print(scale2)

# ------------------------------------------------------------------------

import random       # libs

computer_num = random.randint(1,5) # 1 ----- 10        #cmp number
user_num = int(input("Enter a number [1,5] : ")) #usr_input_num --23

if user_num <= 5:
    if computer_num > user_num:
        print(f"Computer win. cp {computer_num} | usr {user_num}")
    elif computer_num < user_num:
        print(f"User win. cp {computer_num} | usr {user_num}") 
    elif computer_num == user_num:
        print(f"Draw. cp {computer_num} | usr {user_num} ")  
    else:
        print("Something Wrong. Try again.")
else:
    print("Sorry, you can input between 1 to 10.")
