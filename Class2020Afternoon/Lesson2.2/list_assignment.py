# list methods assignment
# use the del statement to delete an element at a specific index
list1 =['physics','chemistry',1997,19090]
print(list1)
del list1[2]
print(list1)
# insert() - inserts an element at specified position
# syntax list.insert(position,element)
list2 = ['mathematics', 'biology', 2000,2015]
list2.insert(2,'physics')
print(list2)
# extend() - to add contents of one list to another list
# syntax - list1.extend(list2)
list3 =[1,2,3,4]
list4 = [6,8,9]
list3.extend(list4)
print(list3)
# sum() - calculates the sum of all the lements of list
# syntax - sum(list)
list5 = [3,4,5,8,9]
print(sum(list5))
# count() - calculates the total occurences of given element of list
# syntax list.count(element)
list_gen = [1,2,3,4,5,6,7,8,9,12,3,6,7,78,90,40]
print(list_gen.count(7))
# len() - calculates the lenth of the list
# len(list_name)
print(len(list_gen))
# index() - return the index of the first occurence. start and end index are not necessary parameters
# syntax -  list.index(element[,start[,end]])
print(list_gen.index(40))
# min() calculates minimum of all elements of list
# syntax - min(list)
min(list_gen)
# max() - calculates the maximum of all the elements of the list
# syntax max( list)
print(max(list_gen))
# reverse() sort the given data structure(both tuple and list) in ascending order
# key and reverse_flag are not necessary parameters and the reverse_flag is set to false , if nothing is passed through sorted()
# syntax - sorted([list[,key[,reverse_flag]]])
# list.sort([key,[reverse_flag]])
list_gen.sort()
print(list_gen)
list_gen.reverse()
print(list_gen)

# deletion of list elements built in functions that can be used include pop() & remove() and keyword such as del
# pop() - the index parameter is optional if not assigned the last element of the ist is popped
# syntax - list.pop([index])
list_gen.pop(2)
print(list_gen)
# del() elements to be deleted is mentioned using a list name and index
# syntax - del list.[index]
del  list_gen[1]
print(list_gen)
# remove() - element to be deleted is mentioned using list name and element
# syntax - list.remove(element)
list_gen.remove(6)
print(list_gen)
# "in " operator - this is used to check if an element is present in the list or not. Returns true if an element is present in the list else returns false
# "not in" checks if an element is not present in the list or not. it returns if element is  not present in the list else returns false
# code to demonstarte working of "in" and "not in"
if 4 in list_gen:
    print("the list is having 4 as an element")
else:
    print("list doesnt contain a four")
# operator "+" is used to concatenate two list into a single list
# "*" operator is used to multiply the list "n" times and then return the single list
lis = list1 + list2
print(lis)
# clear() -  this is used to erase all the elements of list. after this the list becomes empty
# python code for demonstrating sorting and removal of list duplicates
# demo- using sorted() + set() + count()
test_list = [5,6,2,3,5,6,89,5,4,3,1,2,3,4]
res = sorted(set(test_list),key = lambda ele: test_list.count(ele))
print(res)
print("this is a sorted list :"+str(res))
# tuple is similar to a list except that it is a fixed-lenth and immutable
# so values of a tuple cannet be changed nor can values be added or removed from the tuple
# used for small collection of values that cannot be changed for instance ip addresses and port numbers
ip_address = ('10.20.30.40', 8080)
# a atuple with only one member must be defined(note the comma) this way
one_member_tuple = ('only member',)