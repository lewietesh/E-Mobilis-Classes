# inheritance is a way of subclass making a copy of or methods and variables from a class(parent/super)
class Animal:
    def __init__(self,name,origin,num_legs, dangerous =True ):
        self.name =name
        self.origin = origin
        self.num_legs = num_legs
        self.dangerous = dangerous
    def sound(self):
        print("Moooooo")
    def move(self):
        print("can walk")
    def printDetails(self):
        print("Name: {}".format(self.name))
        print("origin: {}".format(self.origin))
        print("number of legs: {}".format(self.num_legs))
# child class
# in the child class pass in the class name that you want to inherit from
class WildAnimals(Animal):
    def __init__(self,name,origin,num_legs,dangerous =True):#removes inheritance
        self.name   =name
        self.origin    =origin
        self.num_legs =num_legs


# access variable and the number of legs
wolf= WildAnimals("werewolf","Asia",4)
wolf.printDetails()
class DomesticAnimal(Animal):
    def __init__(self, name,origin,num_legs,owner,dangerous=True):# removes inheritance
        Animal.__init__(self,name,origin,num_legs)
        self.owner =owner
goat =DomesticAnimal("mike","uk",4,'paul',dangerous=False)
goat.sound()
goat.move()
goat.printDetails()