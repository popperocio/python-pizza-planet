import random
from faker import Faker
from .constants import MIN_DATE, MAX_DATE


fake = Faker()


def generate_clients(number_clients):
    clients = []
    for _ in range(number_clients):
        clients.append({
            "client_address": fake.address(),
            "client_dni": fake.random_number(digits=10),
            "client_name": fake.name(),
            "client_phone": fake.phone_number(),
        })
    return clients


def generate_order(clients, ingredients, beverages, sizes):
    client = random.choice(clients)
    size = random.choice(sizes)
    order_date= fake.date_time_between(
            start_date=MIN_DATE, end_date=MAX_DATE, tzinfo=None)
    print(order_date)
    order = {
        'client_name': client["client_name"],
        'client_dni': fake.random_number(digits=10),
        'client_address': fake.address(),
        'client_phone': fake.phone_number(),
        'date': order_date.strftime('%Y-%m-%d %H:%M:%S'),
        'size_id': size[0], 
    }
    size_price =float(size[2])
    ingredients= generate_ingredient(ingredients)
    beverages= generate_beverages(beverages)
    total_price = calculate_total_price(
        size_price, ingredients, beverages)
    print(order)

    return order, ingredients, beverages, total_price


def calculate_total_price(size, ingredients, beverages):
    print(size)
    total_price: float = float(size)
    if ingredients:
        for ingredient in ingredients:
            total_price += float(ingredient["ingredient_price"])
    if beverages:
        for beverage in beverages:
            total_price += float(beverage["beverage_price"])
    return total_price


def generate_ingredient(ingredients):
    ingredient_details = []
    num_ingredient_details = random.randint(2, 6)
    for _ in range(num_ingredient_details):
        ingredient = random.choice(ingredients)
        ingredient_id, ingredient_name, ingredient_price = ingredient
        ingredient_details.append({
            "ingredient": {
                "_id": ingredient_id,
                "name": ingredient_name,
                "price": float(ingredient_price),
            },
            "ingredient_price": float(ingredient_price)
        })

    return ingredient_details


def generate_size(sizes):
    size = random.choice(sizes)
    size_id, size_name, size_price = size
    size_details = {
        "size": {
            "_id": size_id,
            "name": size_name,
            "price": float(size_price),
        },
        "size_price": float(size_price)
    }
    print("**", size_details)
    return size_details


def generate_beverages(beverages):
    beverage_details = []
    num_beverage_details = random.randint(2, 6)
    for _ in range(num_beverage_details):
        beverage = random.choice(beverages)
        beverage_id, beverage_name, beverage_price = beverage
        beverage_details.append({
            "beverage": {
                "_id": beverage_id,
                "name": beverage_name,
                "price": float(beverage_price),
            },
            "beverage_price": float(beverage_price)
        })
