import datetime

# python is one of oop languages just like java, kotlin etc
# almost everything in python is an object
# a class is a blueprint for creating objects
# use the keyword "class" to create a class in python
# class names must start with an uppercase
# class names can only be in singular

class Car():#the parenthesis is optional still class Car: is correct
    # properties or fields are variables in a class
    def __init__(self,brand,color,size,capacity,automatic):
        self.brand = brand
        self.color = color
        self.size = size
        self.capacity = capacity
        self.automatic = automatic
    def move(self):
        print("moving at 100 km/hr")
    def drift(self):
        print("Drifting in circles")
    def honk(self):
        print("piii piii piiiiiiiiiiiiiiii")
    def printDetails(self):
        print("Brand: {}".format(self.brand))
        print("color: {} ".format(self.color))
        print("size: {}".format(self.size))
        print("automatic: ".format(self.automatic))


# class is a blueprint of objects
# an object is a copy of a class

c1 =Car('Audi','blue','huge',5,False)
c1.printDetails()
# (): the parenthesis act as a constructor

print(c1.honk())
print(c1.drift())
print(c1.move())
# to acces properties in and methids in a class we use the dot operator(.)
c1.size
print(c1.size)
# changing object property
c1.brand
print(c1.brand)

class Person:
    # init function assigns values to variables
    # assign data to object variables
    def __init__(self,name,age,studentID):
        self.name = name
        self.age= age
        self.studentID=studentID
    def yearOfBirth(self):
        current_datetime = datetime.datetime.now()#  datetime = module
        current_year = current_datetime.strftime("%Y")
        current_year =int(current_year)
        Y_O_B = current_year -self.age
        print("year of birth is {}".format(Y_O_B))
        print(current_datetime)

student = Person("John Doe",23,"12345678")
print(student.name)
print(student.age)
print(student.studentID)
c1.printDetails()
new_student = Person('Lewis',20,"12345")
new_student.yearOfBirth()
print(new_student.yearOfBirth())




