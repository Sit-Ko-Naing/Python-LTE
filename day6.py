#IF___ELIF-___else

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
opr = input("Press A to add, M to multiply, S to sub, D to divided.")

if opr == "A":
    sum = num1 + num2
    print(f"Total value is {sum}")
elif opr == "M":
    sum = num1 * num2
    print(f"Total value is {sum}")
elif opr == "S":
    sum = num1 - num2
    print(f"Total value is {sum}")
elif opr == "D":
    if num2 == 0:
        print("Yon can't divided with zero.")
    else:
        total = num1 / num2
        print(f"Total value is {total}")
else:
    print("Something wrong")