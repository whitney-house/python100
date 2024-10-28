from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_coffee_machine = CoffeeMaker()
my_cashier = MoneyMachine()
my_menu = Menu()

is_on = True
while is_on:
    items = my_menu.get_items()
    choice = input(f"What would you like? ({items}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_machine.report()
        my_cashier.report()
    else:
        order = my_menu.find_drink(choice)   # <menu.MenuItem object at 0x1051ab6a0>
        if my_coffee_machine.is_resource_sufficient(order):
            # get_money = my_cashier.process_coins()
            # if my_cashier.make_payment(get_money):
            #     my_coffee_machine.make_coffee(order)

            if my_cashier.make_payment(order.cost):
                my_coffee_machine.make_coffee(order)








