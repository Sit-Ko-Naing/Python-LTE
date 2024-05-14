#Import math library
import math

#Round a number upward to its nearest integer
print(math.ceil(3.3))

# ____________________________________________________________

#Import math library
import math

#Round a number downward to its nearest integer
print(math.floor(3.3))

# ____________________________________________________________

# Import math Library
import math

#Return the value of 9 raised to the power of 3
print(math.pow(4, 3))

# _________________________________________________________

# Import math Library
import math

#Return the value of 9 raised to the power of 3
print(math.sqrt(9))

# ___________________________________________________________

#Import math library
import math

#find the  the greatest common divisor of the two integers
print (math.gcd(4, 12))

# __________________________________________________________

#Import random library
import random

#find the range
print (random.randrange(3, 6))

# ____________________________________________________________________

#Import random library
import random

#Return the randomly selected element
mylist = ["Zaw Nay Lin", "TT", "instructors"]
print(random.choice(mylist))

# ___________________________________________________________

#Import random library
import random

#Return the randomly shuffled sequence
mylist = ["Zaw Nay Lin", "TT", "instructors"]
random.shuffle(mylist)
print(mylist)

# _______________________________________________________________

import tmp_module

tmp_module.greeting()

from tmp_module import image
from tmp_module import *


# ______________________________________________________________

import tmp_module

num1 = int(input("sfsk"))
num2 = int(input("sfsxzc"))


reslt = tmp_module.calc(num1,num2)
print(reslt)
