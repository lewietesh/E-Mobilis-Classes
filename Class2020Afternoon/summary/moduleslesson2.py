# to borrow code from a file use import keyword

import platform
import os
# importing a sepecific code
from lesson1 import country
# print(lesson1.country)
incoming_list = lesson1.my_list
print(incoming_list)
lesson1.greetings()

print(platform.system)
print(platform.machine)
print(os.getcwd())# working folder
dir = os.getcwd()
#os.mkdir(dir+"/"+"lesson3")
#os.mknod(dir +"/lesson3/" +"lesson3.py")
#os.mkdir(dir+"/"+"Javascript")
os.mknod(dir +"Javascript"+"jquery.js")