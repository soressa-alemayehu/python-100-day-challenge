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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def reporter():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffe: {resources['coffee']}g")

def is_resource_sufficient(order_items):
    for item in order_items:
        if order_items[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_payment():
    print("please inser a coin")
    quarter = int(input("how many quarters "))
    dime = int(input("how many dime "))
    nickels = int(input("how many nickels "))
    penny = int(input("how many penny "))

    return (0.25*quarter + 0.1*dime + 0.05*nickels + 0.01*penny )
def check_transaction(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"here is your change {change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_name, order_items):
    for item in order_items:
        resources[item] -= order_items[item]
    print(f"here is your {drink_name}")

is_on = True
while is_on:

    choice = input("what would you like ?(esperesso/ latte / cappuccino)")

    if choice == "off":
        is_on = False
    elif choice == "report":
        reporter()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_payment()
            if check_transaction(payment, drink["cost"]):
                make_coffe(choice , drink["ingredients"])


