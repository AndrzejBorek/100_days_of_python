from Menu import Menu, MenuItem
from CoffeeMaker import CoffeeMaker
from money_machine import MoneyMachine



def Coffe_Machine():

    money_machine = MoneyMachine()
    menu = Menu()
    coffee_maker = CoffeeMaker()
    is_on = True
    while is_on:
        options =  menu.get_items()
        choice = input(f"What coffee would you like?\n{options}\n")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            coffee = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    coffee_maker.make_coffee(coffee)

    