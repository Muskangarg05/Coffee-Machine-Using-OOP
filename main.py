''' Importing classes from modules '''
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

''' Creating objects for classes '''
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

''' Flag to keep the machine running '''
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like {options}")
    
    if choice == "off":
        is_on = False
        
    elif choice == "report":
        ''' Show current ingredient levels '''
        coffee_maker.report() 
        ''' Show money earned so far ''' 
        money_machine.report() 
        
    else:
        ''' Get drink details (ingredients, cost) '''
        drink = menu.find_drink(choice)
        
        ''' Check resources and process payment and Make the coffee  '''
        if (coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)