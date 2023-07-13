import sqlite3
from utils import(
    generate_clients,
    generate_order,
    NUMBER_CLIENTS,
    NUMBER_ORDERS,
    INGREDIENTS,
    BEVERAGES,
    SIZES
    )


conn = sqlite3.connect('pizza.sqlite')
cursor = conn.cursor()

clients = generate_clients(NUMBER_CLIENTS)

def insert_seed_order(cursor, order, total_price):
    cursor.execute("""
        INSERT INTO `order` (`client_name`, `client_dni`, `client_address`, `client_phone`, `date`, `total_price`, `size_id`)
        VALUES (?, ?, ?, ?, ?, ?, ?)
     """, (order['client_name'], order['client_dni'], order['client_address'],
                 order['client_phone'], order['date'], float(total_price), order['size_id']))
     
     
def insert_seed_size(cursor, size):
    cursor.execute('''
        INSERT INTO size (_id, name, price)
        VALUES (?, ?, ?)
    ''', (size))


def insert_seed_ingredient(cursor, ingredient):
    cursor.execute('''
        INSERT INTO ingredient (_id, name, price)
        VALUES (?, ?, ?)
    ''', (ingredient))

    
def insert_seed_beverage(cursor, beverage):
    cursor.execute('''
        INSERT INTO beverage (_id, name, price)
        VALUES (?, ?, ?)
    ''', (beverage))


for order in range(NUMBER_ORDERS):
    order, ingredients, beverages, total_price = generate_order(
        clients, INGREDIENTS, BEVERAGES, SIZES)
    insert_seed_order(cursor, order, total_price)
   

conn.commit()
conn.close()









