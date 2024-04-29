#Nested List
classA = ["ko ko","Aung Aung"]
classB = ["kyaw kyaw","maung maung"]
classC = ["Aye Aye","Hla hla"]

grade10 = [classA,classB,classC]

print(grade10)
print(len(grade10))
print(grade10[0][1])   #Aung Aung

# -----------------------------------------------------------------------------

#Tuple ==> ()
#tuple ===> ordered structure


tuple_container = (1,2,3,4,5)
print(tuple_container)
print(tuple_container[::-1]) #reverse

#tuple packing
student_marks = 450,500,430,330
print(student_marks)
print(type(student_marks))

#tuple unpacking
student_one,student_two,student_three,stdent_four = student_marks
print(student_one)
print(student_two)
print(student_three)
print(stdent_four)

# ---------------------------------------------------------------------------------------------------------------

#difference between List vs Tuple

# List is mutable

# listA = [1,2,3]
# print(listA)
# listA[2] = 5
# print(listA)

# #Tuple is immutable
# tupleA = (1,2,3)
# print(tupleA)
# tupleA[2] = 7    #Error
# print(tupleA)

# -------------------------------------------------------------------------------------------------------------------

t1 = (1,2,3)
t2 = (4,5,6)

t3 = t1 + t2

print(t3)

# ---------------------------------------------------------------------------------------------------------------

#Tuple Method (count,index)

tu1 = (1,2,3,3,4,3,4,5,2,2,3,4,2,2,3,5)
count = tu1.count(1)
index = tu1.index(5)

print(index)

# --------------------------------------------------------------------------------------------------------------------------

import sys

L1 = [1,2,3,4,5]
T1 = (1,2,3,4,5)

print(sys.getsizeof(L1))
print(sys.getsizeof(T1))        #byte unit

# -----------------------------------------------------------------------------------------------------------------------------

#while loop

i = 10

while i > 10:
    print("Hello world.")
    i -= 1


# ----------------------------------------------------------------------------------------------

# for loop  | while loop | do while loop

import random

player1 = 0
player2 = 0

is_game_on = True

while is_game_on:
    player1 = player1 + random.randint(1,100)
    player2 = player2 + random.randint(1,100)

    if player1 > 100:
        print(f"Player1 win the game with {player1} marks")
        is_game_on = False
    elif player2 > 100:
        print(f"Player2 win the game with {player2} marks")
        is_game_on = False

# ---------------------------------------------------------------------------