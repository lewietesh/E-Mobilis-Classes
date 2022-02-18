# python dictionaries
# is a collection of item in keys and value pairs
# is unordered
# changeable
# indexed
age ={
    "john": 21,
    "mary": 34,
    "paul": 56
}
candidate ={} #an empty dictionary
candidate= dict()
# accessing values in a dictionary
# use keys to access values
print(age['john'])
print(age['mary'])
print(age['paul'])
# get() method
print(age.get('john'))
# changing dictionary values
# use key to change values
age['john'] = 31
age['mary'] =44
age['paul'] = 66
print(age)
print(age.get('john'))
print(age.values())
print(age.keys())
# looping through dictionaries
# checking if a value exist in a dictionary
if 'john' in age:
    print("john exist")
# checking the lenth of a dictionary: use the len()
ages =len(age)
print(ages)
# dictionary methods/function
# adding items in a dictionary
age['dem'] =12 # adding item in a dictionary
print(age)
# removing items from a dictionary: use pop()
#age.pop('paul')
print(age)
get_paul = age.pop('paul')
print(age)
print(get_paul)
get_no = age.popitem()
print(get_no)

event ={
    "piano": 1,
    "guitar": 7,
    "drum":9,
    "host": "wanyama"
}
# popitem(): removes the last item
event.popitem()
print(event)
# Assignment:
# copying a dictionary
# deleting a dictionary
# updating a dictionary
people =[
    {'john':21,'mary': 34, "paul":45},
    {"john":"kenya", "mary":"UK", "paul":"UG"},
    {'languages':['python','PHP','Java']}

         ]
print(people[0])
print(people[0]['mary'])
print(people[1]['paul'])
print(people[2]['languages'][0])

# tuple dtypeata collection which is ordered, unnchangeable
# written using round brackets ()
fruits= ('apples','mango','melon','pinnaple','orange','banana','avocado')
print(fruits[4])
# slice a tuple
new_tuple =slice(fruits,2)
print(new_tuple)
# assignment
# joining two tuples
