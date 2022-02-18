# comparison operators - used to compare values
# the return value for these operators is boolean
# ==, !, >,<,<=,>=
# == equals
t= 100
s = 50
print(t==s)

# != Not Equal to
print(t!=s)

# > Greater than sign
print(s>t)
print(t>s)
# Logical operators
# used to combine conditional statements
# AND : returns true if both statements are true and false if either or both of them are false
user_email = "demo@gmail.com"
user_password ="pass1234"
db_email = "demo@gmail.com"
db_password = "pass1234"
if user_email== db_email  and user_password==db_password:
    print(" you have successfully logged in")
else:
    print(" incorrect login details")

# OR :Returns true if one statement is true
c= 5
print(c>3 or c<4)

# NOT : reverses the results, returns false if the result is true
print(not(c>3 or c<4))
#  write a code that proves that 31 is an odd number
n= 31
if n%2==0:
    print("{} is an even number".format(n) )
else:
    print("{} is an odd number".format(n))
# write a program that proves that 32 is an odd number

# ORM

