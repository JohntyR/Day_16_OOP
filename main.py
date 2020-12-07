from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem

coffemaker = CoffeeMaker()
coffemaker.report()
my_menu = Menu()


while True:
    print(f"Hi, what would you like {my_menu.get_items()}?")
    userInput = input()
    if userInput == "off":
        break
    elif userInput == "report":
        coffemaker.report()
    else:
        drink = my_menu.find_drink(userInput)
        if isinstance(drink, MenuItem):
            if coffemaker.is_resource_sufficient(drink):
                coffemaker.make_coffee(drink)

        del drink