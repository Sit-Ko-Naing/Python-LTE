# students = []
# answer = "Y"
# while answer == "Y":
#    name = input("Enter the student's name:")
#    students.append(name)
#    answer = input("Continue? Y/N ")
# print(students)


# -----------------------------------------------------------------------------



# option = "Y"

# while option == "Y":
#     num1 = int(input("Enter num1: "))
#     num2 = int(input("Enter num2: "))
#     opr = input("Press A to add, M to multiply, S to sub, D to divided.")

#     if opr == "A":
#         sum = num1 + num2
#         print(f"Total value is {sum}")
#     elif opr == "M":
#         sum = num1 * num2
#         print(f"Total value is {sum}")
#     elif opr == "S":
#         sum = num1 - num2
#         print(f"Total value is {sum}")
#     elif opr == "D":
#         if num2 == 0:
#             print("Yon can't divided with zero.")
#         else:
#             total = num1 / num2
#             print(f"Total value is {total}")
#     else:
#         print("Something wrong")

#     option = input("Continue? Y/N ")

# print("Thank for using my program.")

# --------------------------------------------------------------------------------------------

# BREAK

# lst = [1,2,3,4,5,6,7,8,9]
# for num in lst:
#     if num != 5:
#         print(f"Valid Number ==> {num}")
#     else:
#         # break #   stop the whole looping
#         # continue
#         pass
#         print(f"Invalid number {num}")


# ----------------------------------------------------------------------------------------

#PASS

# def function():
#     pass

# function()

# ----------------------------------------------------------------------------------------

# for val in "Python":
#     if val == "h":
#         continue
#     print(val)
# print("Out of for loop!!!")

# -----------------------------------------------------------------------------------------

numberss = [10,20,3,14,52,123,22]
result = 1

for num in numberss:
    if num == 123:
        continue
    result = result * num

print(f"the result is : {result}")