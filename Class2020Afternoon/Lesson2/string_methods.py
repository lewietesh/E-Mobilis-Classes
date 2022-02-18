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
# syntax str.replace(old,new[,max]) Example
str1 = 'I am  Johnie Walker.I love drinking. I like being nasty '
print(str1)
print (str1.replace('I', 'We',2))
# find("string",beg,end) -this method is sud to find the position of the substring within a string
# It takes three arguments, substring, starting index(0 by default) and the ending index(by default string length)
# it returns "-1 " if the string is not found in the given range
# it returns the first occurence of string if found
my_string = "geeks for geeks is for geeks only, that means only geeks can use the platform with other "
str ="geeks"
# using find() to find first occurrence of str

print("The first occurrence of str2 is at : ")

print(my_string.find(str))
print(my_string.find(str,1,16))
# rfind finds the last occurence of the substring
print(my_string.rfind(str))
# startswith("string",beg,end) - This returns true if the function bgins with mentioned string
# else return false.
# endwith("string", beg,end) - this returns true if the function ends with the mentioned string(suffix) else returns false
# python code to demo working of startswith() and endswith() function
new_string = "geeks"
new_string2 = "geeksforgeeks"
if new_string2.startswith(new_string):
    print("new_string2 starts with :" + new_string)
else: print("new_string2 does not begin with :"+new_string)
# using endwith function
if new_string2.endswith(new_string):
    print("new_string2 ends with :" + new_string)
else:
    print("new_string2 does not end with :" + new_string)
# islower("string") this function retruns true if all the letters in  the string are lower cased, otherwise false
# isupper("string)
# lower() this returns the new string with all the letters converted into its lowercase
# upper() this returns the nwe string with all the letters converted into its uppercase
# swapcase() this is used to swap cases of string i.e uppercase is converted to lowercase and viceversa
# title() this converts string to its title case i.e  first letter of everyword is uppercased and the lest lower case
# usage of upper() function
demo =" welcome to kenya the pride of africa"
upper_demo =demo.upper()
lower_demo = upper_demo.lower()
print(lower_demo)
print(upper_demo)
title_demo = demo.title()
print(title_demo)
demo = "WelCome TO our HOMELAND and MOTHERLAND africa"
print(demo)
swap_demo = demo.swapcase()

print(swap_demo)
# rstrip() -removes all trailing whitespace of string
# strip() removes trailing and following characters after a string by default whitespaces trailing are removed
# split(separator, maxsplit) method splits a string into a list
# maxsplit  specifies how many splits to do.Default value is -1 whis is " all occurences"
# you can specify the separator by default is any whitespaces
# min("string") this return the minimum value alphabetical
# max("returns maximum value alphabet")

