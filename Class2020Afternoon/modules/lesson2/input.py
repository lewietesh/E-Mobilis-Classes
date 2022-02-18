# used to prompt users to enter data  for processing
# input() function used to grab data
# input() function converts data into a string by default
name = input("please enter your name:") #prompts data from the user
age = int(input("please enter your age: "))
country = input("please enter your country:")
user_dict = {
    "name": name,
    "age": age,
    "country": country
}#dictionary
user_list =[name,age,country]#list
user_tuple =(name,age,country)#tuple
user_set = {name,age,country}#set
print("Dictionary",user_dict)
print("List",user_list)
print("Tuple", user_tuple)
print("Set", user_set)
# print(type(age))

if age<18:
    print("Hello {}, you are underage".format(name))
elif age>=18 and age!=30:
    print("hello {}, your age {} limit is allowed".format(name,age))

