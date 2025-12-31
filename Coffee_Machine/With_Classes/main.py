from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_card = Menu()
drinks = CoffeeMaker()
payment = MoneyMachine()

is_on = True

while is_on:
    order = input(f"What would you like to drink: {menu_card.get_items()} ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        drinks.report()
        payment.report()
    else:
        drink = menu_card.find_drink(order)
        if drinks.is_resource_sufficient(drink):
            if payment.make_payment(drink.cost): #passing the cost of the drink
                drinks.make_coffee(drink)