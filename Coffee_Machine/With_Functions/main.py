from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

revenue = 0

def report():
    for i in resources:
        print(f"{i}: {resources[i]}")

def is_ingredients_sufficient(order_ingredient):
    for i in order_ingredient:
        if order_ingredient[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def insert_coins():
    print("Please insert coins:")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_successful_transaction(money_received,drink_cost):
    if money_received > drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Please collect change: ${change}")
        global revenue
        revenue += drink_cost
        return True
    else:
        print("Not enough change, money refunded. Please reorder")
        return False

def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        report()
        print(f"Revenues: ${revenue}")
    else:
        drink = MENU[order]
        if is_ingredients_sufficient(drink["ingredients"]):
            payment = insert_coins()
            if is_successful_transaction(payment, drink["cost"]):
                make_drink(order, drink["ingredients"])
