#Sequential Statement
#Conditional Statement
#Looping/Iteration Statement

#for loop/while loop

for i in range(5):
   print("Hello world")
# ------------------------------------------------------------------------

lst = [1,2,3,4,5.2,6,7,"mgmg"]

for i in lst:
   print(i)

# --------------------------------------------------------------------------

#PythonTutor

# -----------------------------------------------------------

test_container = range(0,10)
print(list(test_container))

# ----------------------------------------------------

#Exercise

# Write a program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of 
# number and for multiples of five print "Buzz".For number which are multiples of both three and five print "FizzBuzz"

# -----------------------------------------------------------------------------

# num = 0

# for i in range(0,13):
#     num = 5 * i
#     print(num)

# for i in range(0,5): # 0 1 2 3 4 
#     print(f" {i} - Hello World!")

# print("Hello, outside block.")



num = 0

for i in range(1,11):
    num = num + 1
    print(f"{num} for loops.")

print(f"the last value of {num}")
