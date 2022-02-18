try:#  lets you test a block of code for errors
    print(a)
except:# handles the rror that has occured
    print("An exception occured")
# specifyimg the type of error

try:
    print(b)

except NameError:#explicit error identification
    print("this is a name error")
except TypeError:
    print("this is a type error")
except:
    print("I also do not know the error")
else: #if the try block does not have any errors
    print("nothing went wrong")
finally: #will be executed if the is an error or if there is no errors
    print("I will run no matter what")
x=-1
if x<2:
    raise Exception("hello, error occured")