#Dictionary Datatype {}
# key:value
#unorder data structure

phone_book = { "Aung Aung"   : 123,
              "Maung Maung"  : 456,
              "kyaw kyaw"    : 789
             }

print(phone_book)
print(type(phone_book))
print(phone_book["Aung Aung"])
print(phone_book["kyaw kyaw"])

# key must be unique
# value is not

phone_book = { "Aung Aung"   : 123,
              "Maung Maung"  : 456,
              "kyaw kyaw"    : 789,
              "kyaw kyaw"    : 111
             }

print(phone_book)

phone_book = { "Aung Aung"   : 123,
              "Maung Maung"  : 456,
              "kyaw kyaw"    : 789,
              "pai pai"      : 789
             }

print(phone_book)

# _____________________________________________________________________________________

#Constructor ( dict () )

phone_num = dict()
phone_num["Aung"] = 2323
phone_num["kyaw"] = 1212
phone_num["pai"]  = 3434
phone_num["Maung"] = 4545


print(phone_num)

# ___________________________________________________________________________________________

#Nested Dict

books = {'Aung Aung' : ['English','Science'],
         'Kyaw Kyaw' : ['Bio','Physics'],
         'Ko Ko'     : ['Physics','Chemistry'],
         2001        : ['java','cpp','python']
        }


print(books["Ko Ko"][1])

# ________________________________________________________________________________

books1 = {'Ma Ma' : {'read' : ["history","Psycho"],
                     'unread' : ["Eco","Bio"]
                    },
          'Ni Ni' : {'read' : ["harry poter","lucifer"],
                     'unread' : ["streelife","atomic habits"]
                    }
        }

print(books1["Ni Ni"]['unread'][1])

# _____________________________________________________________________________________________

#Dict Operation
#mutable

#adding and updating dict

phone_book = { 
              "Aung Aung"    : 123,
              "Maung Maung"  : 456,
              "kyaw kyaw"    : 789
             }

phone_book["ko ko"] = 765

print(phone_book)

phone_book["Aung Aung"] = 231

print(phone_book)


#deleting dict
delete_usr = phone_book.pop('kyaw kyaw')
delete_usr_item = phone_book.popitem()
del(phone_book["Aung Aung"])

print(phone_book)
print(delete_usr)
print(delete_usr_item)

# _________________________________________________________________________________

#in keyword (checking key existence)

phone_book = { 
              "Aung Aung"    : 123,
              "Maung Maung"  : 456,
              "kyaw kyaw"    : 789
             }

print("kyaw kyaw" in phone_book)

# ______________________________________________________________________________

#copying content

phone_book = { 
              "Aung Aung"    : 123,
              "Maung Maung"  : 456,
              "kyaw kyaw"    : 789
             }

phone_book2 = {"mi mi" : 876}
phone_book.update(phone_book2)

print(phone_book)

# ____________________________________________________________________________________

#set data type {}

my_dict = {'mg mg':"yangon"}
print(type(my_dict))

my_set = {'mg mg','yangon'}
print(type(my_set))

#no indexing #unorder data structure
#we can't access by index number
#can store immutable data

my_set1 = {1,1,1,1,1,2,3,2,2,3,2,1}
print(my_set1)

#set not accept duplicate data
#unorder data structure

my_set2 = {23,232,323,232,232,32,32,2323,23,2,32,32,3,23,223,23,23,23,2,23,23,23,23,23,23,323,2,3}
print(my_set2)


#list to set

lst1 = [23,32,23,2,32,32,23,23,23,3,232,3,23,23,23,23,23,23]
set1 = set(lst1)
print(set1)

# _____________________________________________________________________________________________________________/

#add method

empty_set = set()
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
empty_set.add(4)

print(empty_set)

empty_set.remove(3)

print(empty_set)

# _______________________________________________________________________

#union set

set_a = {1,2,3,4,5,6}
set_b = {1,2,3,7,8,9}

union_set = set_a.union(set_b)  #union set
print(union_set)

intersection_set = set_a.intersection(set_b)    #intersection set
print(intersection_set)

diff_set = set_a.difference(set_b)
print(diff_set)
