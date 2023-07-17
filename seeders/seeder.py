import sqlite3

from datetime import datetime
import random
from .utils import generate_clients, generate_order, BEVERAGES, INGREDIENTS, NUMBER_CLIENTS, NUMBER_ORDERS, SIZES
from faker import Faker

fake = Faker()


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

def seed():
    connection = sqlite3.connect('pizza.sqlite')
    cursor = connection.cursor()
    for order in range(NUMBER_ORDERS):
        order, ingredients, beverages, total_price = generate_order(
            clients, INGREDIENTS, BEVERAGES, SIZES)
        insert_seed_order(cursor, order, total_price)
    
    for size in SIZES:
        insert_seed_size(cursor, size)

    for ingredient in INGREDIENTS:
        insert_seed_ingredient(cursor, ingredient)

    for beverage in BEVERAGES:
        insert_seed_beverage(cursor, beverage)
    
    connection.commit()
    connection.close()



seed()

