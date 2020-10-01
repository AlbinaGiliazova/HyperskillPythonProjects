# -*- coding: utf-8 -*-
"""
Simulator of a coffee machine. It can run out of ingredients, such as milk or 
coffee beans, it can offer you various types of coffee, and, finally, it will 
take money for the prepared drink.

A project for hyperskill.org

@author: Giliazova
"""
class CoffeeMachine():
    
    d = {"water": 400, "milk": 540, "coffee beans": 120, "disposable cups": 9, 
     "money": 550}
    
    # functions in an alphabetical order
    def ingredients(self, coffee_type):
        if coffee_type == "1":  # espresso
            return {"water": 250, "milk": 0, "coffee beans": 16, 
                           "disposable cups": 1}
        elif coffee_type == "2":  # latte
            return {"water": 350, "milk": 75, "coffee beans": 20, 
                        "disposable cups": 1}
        elif coffee_type == "3":  # cappuccino
            return {"water": 200, "milk": 100, "coffee beans": 12, 
                             "disposable cups": 1}
             
    def make_coffee(self, coffee_type):
        components = self.ingredients(coffee_type)
        for ingredient in components:
            self.d[ingredient] -= components[ingredient]           

    def not_enough_ingredients(self, coffee_type):
        components = self.ingredients(coffee_type)
        for ingredient in components:
            if self.d[ingredient] < components[ingredient]:
                return ingredient
        return False

    def price(self, coffee_type):
        prices = {"1": 4, "2": 7, "3": 6}    
        return prices[coffee_type]

    def print_dict(self):
        print("The coffee machine has:") 
        for thing in self.d:
            if thing == "money":
                print("$" + str(self.d[thing]) + " of " + thing)
            else:    
                print(str(self.d[thing]) + " of " + thing)
                
    def user_input(self, string):
        return input(string)                

# main    
cm = CoffeeMachine()

while True:
    action = cm.user_input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        coffee_type = cm.user_input("What do you want to buy? 1 - espresso, " +\
                                    "2 - latte, 3 - cappuccino, " +\
                                    "back - to main menu:\n")
        if coffee_type == "back":
            continue
        ingredient = cm.not_enough_ingredients(coffee_type)   
        if ingredient:
            print(f"Sorry, not enough {ingredient}!")
        else:
            cm.make_coffee(coffee_type)    
            cm.d["money"] += cm.price(coffee_type)
            print("I have enough resources, making you a coffee!")
    elif action == "fill":
        cm.d["water"] += int(cm.user_input("Write how many ml of water do you want to add:\n"))
        cm.d["milk"] += int(cm.user_input("Write how many ml of milk do you want to add:\n"))
        cm.d["coffee beans"] += int(cm.user_input("Write how many grams of coffee beans " +\
                                   "do you want to add:\n"))
        cm.d["disposable cups"] += int(cm.user_input("Write how many disposable cups of " +\
                                      "coffee do you want to add:\n"))    
    elif action == "take":
        print(f"I gave you ${cm.d['money']}")        
        cm.d["money"] = 0
    elif action == "remaining":
        cm.print_dict()
    elif action == "exit":
        break