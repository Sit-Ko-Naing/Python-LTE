std_list = ["mgmg","kyawkyaw","aungaung","mama","koko","nyinyi"]

value = len(std_list)

print(value)
# ------------------------------------------------------------------------------------

dog_names = ["Mike", "Lucky", "Milo", "Ollie"]
dog_food=["bone","beef","chicken","biscuit"]

print(f"{dog_names[0]} likes {dog_food[3]}")
print(f"{dog_names[1]} likes {dog_food[1]}")
print(f"{dog_names[2]} likes {dog_food[0]}")
print(f"{dog_names[3]} likes {dog_food[2]}")

#ouput
                    # Mike likes bone
                    # Lucky likes beef
                    # Milo likes bone
                    # Ollie likes chicken
# ---------------------------------------------------------------------------------------

dog_names = ["Mike", "Lucky", "Milo", "Ollie"]
dog_food=["bone","beef","chicken","biscuit"]

dog_food.append("vitamins")

print(f"{dog_names[1]} needs {dog_food[1]} and {dog_food[-1]}")
print(f"{dog_names[2]} needs {dog_food[0]} and {dog_food[-1]}")


# Lucky needs beef and vitamins
# Milo needs bone and vitamins
# ------------------------------------------------------------------------------------------------

dog_names = ["Mike", "Lucky", "Milo", "Ollie"]
dog_food=["bone","beef","chicken","biscuit"]

dog_food.insert(0,"salmon")

print(f"{dog_names[2]} now eats {dog_food[0]}")

# --------------------------------------------------------------------------------------------------------

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

weekdays = days[:5]
weekends = days[5:]
with_step = days[::2]

print(weekdays)
print(weekends)
print(with_step)

#ouput
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# ['Sat', 'Sun']
# ['Mon', 'Wed', 'Fri', 'Sun']

# ---------------------------------------------------------------------

list_a = list(range(10))
list_b = list(range(1,10,2))
print(list_a)
print(list_b)

# ------------------------------------------------------------------------

colors_list = ["red", "green" , "blue"]
usr_colors = input("Enter your color: ") #orange

colors_list.append(usr_colors)
print(colors_list)

# -------------------------------------------------------