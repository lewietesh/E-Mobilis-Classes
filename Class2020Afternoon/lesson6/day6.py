 # functions
# modules
# user input
# try except
# github
# todays work functions
# a function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function
# A function can return data as a result
# a function taking no arguments
def greetings1(): #function definition
    print('hello world')
# a function taking a single argument
def greetings2(name):
    print('hello '+name)
greetings2('lewis')

# a function taking three arguments
def greetings3(name,age):
    print('I am {} and I am  {} years old'.format(name,age))
greetings3('Lewis', 20)
# A function that calculates the sum of two numbers
def summation(x,y):
    sumvalue = x+y
    print(" The sum of {} and {} is {}".format(x,y,sumvalue))
summation(200,198)
# the maximum number of arguments a  function can take is 5
summation(50,100)
# default arguments
def greetings4(name, age,country ='kenya'):
    print("your name is {} and you are {} and you come from {}".format(name,age,country))
greetings4('Lewis',20)
# keyword arguments
def greetings5(name,country,age):
    print('Your name is {}'.format(name))

greetings5(age=23,country='Kenya',name='John')

# arbitrary keyword arguments
# if you do not know how many keyword arguments that will be passed into your function,
# add two asterisk:** before the parameter name in the function definition
def greetings6(**ages):
    print('Your age is {}'.format(ages['john']))
    print(ages)
greetings6(john=23,mary=40,jane=32)

def greetings8(my_dict):
    print(my_dict)
ages ={
    'john':23,
    'mary': 45
}
greetings8(ages)

names =['john','zam','chris','james','lewis','haben']
count =len(names)
for x in range(count):
    print(names[x])
for name in names:print(name)
# function that takes in a dictionary
# a function returning a value
#  to let a function return a value, use the return statement:
def greetings7(name ,age):
    my_dict ={
        "jina": name,
        "miaka": age
    }
    return my_dict
grabbed_data = greetings7("Mike",23)
print(grabbed_data)
# ?function to calculate area of a square
def area_of_square(l):
    area = l**2
    return area
a1 = area_of_square(7)
a2 = area_of_square(14)
print('the area is {} square meters'.format(a1+a2))
print('the area is {} square meters'.format(area_of_square(9)+ area_of_square(12)))
#lambda functions this is a single line function declared with no name which can have any number of arguments,
# but it can only have one expression. such a function is capable of behaving similar;y to a
# regular function declared using the python's def keyword
# syntax
# lambda arguments: expression
def sum_of_two(num1,num2):
    print(num1+num2)
sum_of_two(12,14)
sumOfTwo =lambda num1,num2:num1+num2
print(sumOfTwo(10,20))
# why use a lambda function? the power of a lambda function is better shown when you use them as an anonymous
# function inside another function.
# ay you have a functtion definition that takes one argument,
# and that argument will be multiplied with an unknown number:
def print_details(name,age):
    intenyears =lambda age: age+10


    user_dict ={
        "name": name,
        "age": intenyears(age)
    }
    print(user_dict)
print_details('John',23)

