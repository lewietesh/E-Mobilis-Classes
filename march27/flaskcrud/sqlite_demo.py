import sqlite3
from employee  import Employee
# conn = sqlite3.connect(':memory:') - used to create a in memory database
conn = sqlite3.connect('employee.db')
# creating  a cursor 
c =  conn.cursor()
# c.execute(""" CREATE TABLE employees(
#     first text,
#     last text,
#     pay integer
# )""") 

empl_1 = Employee('John','Doe',20000)
emp_2 = Employee('Jane','Doe', 90000)
# print(empl_1.first)
# print(empl_1.last)
# print(empl_1.pay)

# inserting these object to the database using string formatting its a bad practice actually
#  c.execute("INSERT INTO employees VALUES ('{}','{}',{}).format(empl_1.first,empl_1.last,empl_1.pay")

# Here is the right formatting (METHOD TWO)
c.execute("INSERT INTO employees VALUES (?,?,?)",(empl_1,empl_1.last,empl_1.pay)
conn.commit()
# Here is the second ,method
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first': emp_2.first,'last': emp_2.last,'pay': emp_2.pay})
conn.commit()
#  used to add data into the database 
# c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 50000) ")

# # This submits the changes in order to update the database
# conn.commit()

# c.execute("SELECT * FROM employees WHERE last = 'Schafer'")

# c.fetchmany(5) - The .fetchmany command is used to collect the listed amount of data from the database
#  it return them as a list
# c.fetchall  - returns all the list of elements in a list it doesnt take any parameters
print(c.fetchall())
# commit changes made to the database 
conn.commit()
conn.close()