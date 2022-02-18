#print is a function for outputting data
print("Hello world")
#this is a  python comment
#slicing of a string lesson

compliment = "I love Africa"
print(compliment)
print(compliment[0])
print(compliment[-6:])
print(compliment[2:7])

# variable names
# they start with a letter or an underscore only
#variable names not start with a  number
#it can contain alpha numeric characters(A- Z, 0 9)
#variable names are case sensitive e,g name is not the same as Name

name ="John"
_name ="Mary"
Name ="Bill"
print(name)
print(_name)
print(Name)
name ="Kevin"
_name = "peter"
Name ="Joy"
print(name)
print(_name)
print(Name)
age = 20
print(age)
age_string ="20"
print(age_string)
#type casting string to int
age_to_int = int(age_string)
print(age_to_int)
age_to_string = (str(age_to_int))
print(age_to_string)
#concatenation
name = "Shaw"
age = 40
print("I am "+ str(name) +" and I am "+ str(age) + " year old")