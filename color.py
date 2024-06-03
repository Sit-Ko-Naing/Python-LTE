txt_line = "Red Orange Yellow Green Blue Indigo Violet"
txt_line_split = txt_line.split(" ")

print(txt_line_split)

for i in txt_line_split:
    print(i)

new_path = "color1.txt"
new_file = open(new_path,"w")


new_file.writelines(txt_line_split)
new_file.close()