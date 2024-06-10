# for i in range(0,13):
#     num = 2 * i
#     print(f"Two x {i} = {num}")


for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)