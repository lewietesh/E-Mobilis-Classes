# The below program takes options of food preferences as input and then return restaurants with the options you need for the party

# Constant variable to store variables to be used for final computation of grade
ASSIGNMENT = 45;
EXAM = 55;


# Creating a new Python dictionary for each restaurant with key values 
joe_burgers = {'Vegetarian': "no", 'Vegan': "no", 'Gluten-Free': "no"} 
mainstreet_pizza = {'Vegetarian': "yes", 'Vegan': "no", 'Gluten-Free': "yes"} 
corner_cafe = {'Vegetarian': "yes", 'Vegan': "yes", 'Gluten-Free': "yes"} 
fine_italian = {'Vegetarian': "yes", 'Vegan': "no", 'Gluten-Free': "no"} 
chef_kitchen = {'Vegetarian': "yes", 'Vegan': "yes", 'Gluten-Free': "yes"} 

# take user input on the options they want available for the party in arestaurant
vegetarian = input('Is anyone in your party a vegetarian? enter yes or no: ')
vegan = input("Is anyone in your party a vegan? enter yes or no :")

gluten = input("Is anyone in your party a gluten-free? enter yes or no ")


# restaurant_list = [joe_burgers,mainstreet_pizza,corner_cafe,fine_italian,chef_kitchen]
restaurant_names = ["Joe's Gourmet Burger","Main Street Pizaa Company", "Corner Cafe","Mama's Fine Italian","The Chef's Kitchen"]
# create an empty list that will store availabe restaurants 

available_restaurants = [];

options_picked = [vegetarian,vegan,gluten]
# create a list of dictionaries to store all the restaurants in there
restaurants = [joe_burgers, mainstreet_pizza,chef_kitchen,corner_cafe,fine_italian]


# Below is a for loop to check each restaurants available options and match it against the options the user has picked for their party
for i in restaurant_names:
  # if conditions to check the values input by the user against available options by the restaurant
    if options_picked[0] == "yes" and options_picked[1] == "yes" and options_picked[2] =="yes":
    #  appending the restaurant name to the available_restaurants list if the combination selected is available
      available_restaurants.append("The Chef's Kitchen")
      available_restaurants.append("Corner Cafe")
      break;
    elif options_picked[0] == "no" and options_picked[1] == "no" and options_picked[2] == "no":
            available_restaurants.append("Joe's Gourmet Burger")
            break;
    elif options_picked[0] == "yes" and options_picked[1] == "no" and options_picked[2] == "yes":
            available_restaurants.append("Main Street Pizaa Company")
            break;
    elif options_picked[0] == "yes" and options_picked[1] == "no" and options_picked[2] == "no":
      available_restaurants.append("Mama's Fine Italian")
      break;
    else:
      break;

# output available restaurant choices
print("Here are your restaurant choices")
# looping through the available restaurants
for i in available_restaurants:
  print(i)




