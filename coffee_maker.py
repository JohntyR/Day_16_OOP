class CoffeeMaker:
    def __init__(self):
        self.resources = {"Water": 300, "Milk": 200, "Coffee": 100}

    def report(self):
        print(f"Water: {self.resources['Water']}ml")
        print(f"Milk: {self.resources['Milk']}ml")
        print(f"Coffee: {self.resources['Coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f"here is your {order.name} ☕️.Enjoy!")