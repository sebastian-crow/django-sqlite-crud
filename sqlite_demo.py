import sqlite3
from customer import Customer

# If we need an in-memory database use ":memory:"
# each time our application runs database will be flush from
# the RAM and create new database.

# connection = sqlite3.connect(':memory:')

connection = sqlite3.connect('customer.db')
cursor = connection.cursor()

#cursor.execute("""CREATE TABLE customer(
#    first_name text,
#    last_name text,
#    age integer,
#    city text,
#    country text
#)""")

customer_1 = Customer('Jhon','doe',30,'perth','Australia')
customer_2 = Customer('sara','migel',25,'perth', 'Australia')

cursor.execute("INSERT INTO customer VALUES(?, ?, ?, ?, ?)", # Use question marks instead using regular brace placeholders.
(customer_1.first_name,
customer_1.last_name,
customer_1.age,customer_1.city,customer_1.country))

# Another way to save data properly
cursor.execute("INSERT INTO customer VALUES(:first, :last, :age, :city, :country)",
{'first':customer_1.first_name, 'last':customer_1.last_name, 'age':customer_1.age,
'city':customer_1.city, 'country': customer_1.country})

cursor.execute("SELECT * FROM customer WHERE city=?", ('perth',))

cursor.execute("SELECT * FROM customer WHERE city=:city", {'city':customer_1.city})

connection.commit()

connection.close()
