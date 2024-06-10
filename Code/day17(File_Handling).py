#File Handling

path = "text_file.txt"
my_file = open(path,"r")

print(my_file.read())
# # print(my_file.readline())
# # print(my_file.readlines())
# print(my_file.close())

# ________________________________________________________________

# new_path = "newfile.txt"
# new_file = open(new_path, "w")

# txt_line = "Hello"
# new_file.write(txt_line)
# new_file.close()

# ____________________________________________________________________

# txt = "Hello, this is PY4Y Batch6"
# txt = txt.split(",")
# print(txt)

# __________________________________________________________________

# txt_line = "Red Orange Yellow Green Blue Indigo Violet"
# lst = txt_line.split(" ")

# for i in lst:
#     print(i)

# ____________________________________________________________________

# import os

# print(os.getcwd())
# # os.makedirs("jAva Java\\OOp")
# # os.removedirs("jAva Java\\OOp\\")

# # os.chdir('C:\\Users\\Huawei Matebook 15\\OneDrive\\Desktop\\')

# os.rename("jAva Java\\OOp", "jAva Java\\OOOOOP")

# # print(os.getcwd())
# print(os.listdir())