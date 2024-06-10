path = "text\country_city.txt"
my_file = open(path,"r")
lines = my_file.readlines()
my_dict = {}
line = lines[2].rstrip("\n")
country,city = line.split("/")
my_dict[country] = city
print(my_dict)

