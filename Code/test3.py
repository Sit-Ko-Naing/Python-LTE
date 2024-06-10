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








# if user_num  <= 10:

# else:
#     print("Sorry, you can input between 1 to 10")