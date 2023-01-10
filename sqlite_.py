# Import statements
import sqlite3

# Create connection object
connection = sqlite3.connect('customer_second.db')
cursor = connection.cursor()

# Create table
cursor.execute("""CREATE TABLE customer(
    first_name text,
    last_name text,
    age integer,
    city text, 
    country text
) """)


# Will save a customer record into the database
def create_customer(customer):
    with connection:
        cursor.execute("INSERT INTO customer VALUES (:first, :last, :age, :city, :coutry)",
                       {'first':customer.first_name, 'last':customer.last_name,
                        'age':customer.age, 'city':customer.city, 'country':customer.country})

# Will accept the city of a customer and return a result set
def get_customers(city):
    cursor.execute("SELECT * FROM customer WHERE city=:city", {'city':city})
    return cursor.fetchall()

# Gonna update based on the provided customer's first name and last name
def update_city(customer, city):
    with connection:
        cursor.execute("""UPDATE customer SET city=:city
        WHERE first_name=:first AND last_name=:last""",
        {'first':customer.first_name, 'last':customer.last_name, 'city':city})

def delete_customer(customer):
    with connection:
        c.execute("DELETE FROM customer WHERE first_name=:first AND last_name=:last",
        {'first':customer.first_name, 'last':customer.last_name})

customer_1 = Customer('jhon', 'doe',30,'perth','Australi')
customer_2 = Customer('sara', 'migel',25,'perth','Australia')

create_customer(customer_1)
create_customer(customer_2)

update_city(custimer_1, 'sydney')

customers = get_customers('perth')

print(customers)

connecvtion.close()
