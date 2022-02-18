# string methods
greetings = " Hello world  "
# strip function removes spaces before and after a string
greetings.strip()
print(greetings)
# type() function
print(type(greetings))

# case coversion function - upper()
name = "john"
print(name)
name_upper =name.upper()
print(name_upper)
car ="AUDI"
print(car)
new_car = car.lower()
print(new_car)

county = "nairobi"
c = county[0].upper() + county[1:]
print(c)
county2 ="kiambu"
print(county2)
caps = county2[5].upper()
new_county = county2[:5]
print(new_county + caps)
# replace a character in a string : use replace()
print(county2.replace("k","J"))
# format() function
color ="blue"
car = "Benz"
print("My favorite car is " + car + " is color "+ color)
print("my favorite car is {} and  its color {} ".format(car,color) )
age = 20
print(" I am "+ str(age) + " years old" )
print("I am {} years old ".format(age))
# len
num = len(county2)
print(num)
names ="john mary john peter"
num_count = names.count('john')
print(num_count)

# REsearch three more  string functions and their application in python
# strings are immutable hence updation and deletion of characters is not allowed
# however deletion of an entire string is possible through the use of an in-built keyword called del
# to print quotes we use an escape sequence / to prevent an error
# using raw string to
# ignore escape sequence

# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)
# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)
# reprace() is used to print the string along with the quotes
# syntax str.replace(old,new[,max])
str1 = 'I am Johnie  walker'