# #Set data type {}

# lst1 = [23,32,23,2,32,32,23,23,23,3,232,3,23,23,23,23,23,23]
# set1 = set(lst1)

# print(set1)

# # -------------------------------------------

# empty_set = set()
# empty_set.add(1)
# empty_set.add(2)
# empty_set.add(3)
# empty_set.add(4)

# print(empty_set)

# empty_set.remove(4)
# print(empty_set)

# -----------------------------------------------------

set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}

uni_set = set_a.union(set_b)
print(uni_set)   #{1, 2, 3, 4, 5, 6, 7, 8, 9}

inter_set = set_a.intersection(set_b)
print(inter_set)  #{4, 5, 6}

diff_set = set_a.difference(set_b)
print(diff_set)   #