# Dictionary of each menu item, their ingredients and cost.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# Total number of ingredients in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coin_values = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
}


# Check if there are enough ingredients
# by comparing amount of each ingredient in machine compared with amount needed to make drink
def enough_resources(order_ingredients):
    for ingredients in order_ingredients:
        if resources[ingredients] < order_ingredients[ingredients]:
            print(f'Not enough {ingredients}')
            return False
    else:
        return True

#Check if user has inputted enough money by comparing cost of drink with total amount submitted by user.
#Print change amount
def enough_money():
    total_coins = quarters * coin_values["quarters"] + dimes * coin_values["dimes"] + nickles * coin_values[
        "nickles"] + pennies * coin_values["pennies"]

    if total_coins < MENU[question]["cost"]:
        print('Not enough funds. Money refunded')
        return False
    elif question != "report":
        global money
        money += MENU[question]["cost"]
        change = total_coins - MENU[question]["cost"]

        print(f'Here is ${round(change, 2)} in change.')
        return True

#Subtract the amount of each ingredient needed for the drink from the amount in coffee machines resources.
def use_resources(order):
    for resource in resources:
        resources[resource] -= MENU[order]["ingredients"][resource]

    print(f'Here is your {question}')




machine_off = False
money = 0
while not machine_off:
    #Keep asking user  what they want unless they turn off machine.

    question = input("What would you like? (espresso/latte/cappuccino): ")

    #Break while loop if they ask to turn off machine.
    if question == "off":
        print("Machine is off")
        machine_off = True


    #If they ask for report, print eah resource amount and profit.
    elif question == "report":
        print(
            f'Water: {resources["water"]} \nMilk: {resources["milk"]} \nCoffee: {resources["coffee"]} \nProfit: {round(money, 2)} ')

#If a drink is selected check if enough resources and if enough money inputted.


    else:
        drink = MENU[question]
        if enough_resources(drink["ingredients"]):
            print(f'Please insert ${drink["cost"]}0')
            quarters = int(input('How many quarters? '))
            dimes = int(input('How many dimes? '))
            nickles = int(input('How many nickles? '))
            pennies = int(input('How many pennies? '))

            if enough_money():
                if question != "report":
                    use_resources(question)


