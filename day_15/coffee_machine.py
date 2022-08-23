
from multiprocessing.connection import wait
from time import sleep


def coffee_machine():

    from data_for_coffee_machine import PASSWORD

    coffees_made = {
        "espresso":0,
        "latte":0,
        "cappuccino":0
    }
    
    
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
        "water": 4000,
        "milk": 4000,
        "coffee": 1000,
    }
    

    def admin_mode_menu():
        choose = input("1.Get report from ingredients\n2.Get report from coffee\n3.Go back \n")
        if  choose == '1':
            print(f"Resources: {resources}")
            admin_mode_menu()
        elif choose == '2':
            print(f"Coffees made: {coffees_made}")
            admin_mode_menu()
        elif choose == '3':
            main_menu()
        else:
            print("Wrong value.")
            admin_mode_menu()

    
    def check_if_admin():

            print("You need to enter the password to enter Admin Mode!")
            password = input("Enter the password \n")
            if password == PASSWORD:
                admin_mode_menu()
            else:
                print("Wrong password, you can't enter Admin Mode")
                main_menu()   
    
    
    def increase_number_of_coffee(coffee):
        nonlocal coffees_made
        coffees_made[coffee] = coffees_made[coffee]+1


    def decrease_ingredient(coffee):
        nonlocal resources
        nonlocal MENU
        water_reduce,coffee_reduce,milk_reduce = 0,0,0
        water_reduce = MENU[coffee]["ingredients"]["water"]
        coffee_reduce = MENU[coffee]["ingredients"]["coffee"]
        if(coffee == "cappuccino" or coffee == "latte"):
            milk_reduce = MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= coffee_reduce
        resources["milk"] -= milk_reduce
        resources["water"] -= water_reduce

    
    def check_if_available_resources(coffee):
        nonlocal MENU
        nonlocal resources
        water_use = MENU[coffee]["ingredients"]["water"]
        coffee_use = MENU[coffee]["ingredients"]["coffee"]
        if(coffee == "cappuccino" or coffee == "latte"):
            milk_use = MENU[coffee]["ingredients"]["milk"] 
            if milk_use > resources["milk"]:
                print("Not enough milk!")
                return False
        if water_use > resources["water"]:
            print("Not enough water!")
            return False
        elif coffee_use > resources["coffee"]:
            print("Not enough coffee" )
            return False
        else:
            return True
      

    def chosen_coffee(coffee):
        if check_if_available_resources(coffee):
            decrease_ingredient(coffee)
            increase_number_of_coffee(f"{coffee}")
            print(f"{coffee}")
            sleep(2)
            print(f"Have a nice {coffee}")
            main_menu()
        

    def user_mode_menu(choose):
        if  choose == '1':
            chosen_coffee("espresso")
        elif choose == '2':
            chosen_coffee("cappuccino")
        elif choose == '3':
            chosen_coffee("latte")
        else:
            print("Wrong value!")
            user_mode_menu()
        

    def main_menu():
        nonlocal MENU
        print("Coffee Machine menu, type number to choose option: ")
        choose = input(f"1.Get espresso {MENU['espresso']['cost']}"+
        f"\n2.Get cappucino {MENU['cappuccino']['cost']}" + 
        f" \n3.Get latte {MENU['latte']['cost']}" + 
        " \n4.Admin mode \n")
        if choose == '4':
            check_if_admin()
        elif choose == '1' or choose == '2' or choose == '3':
            user_mode_menu(choose)
        else:
            print("Wrong value! ")
            main_menu()


    main_menu()
#---------------------- Here function coffe_machine() is ended


coffee_machine()