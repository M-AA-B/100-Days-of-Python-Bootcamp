# Coffee Machine

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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
MONEY = 0
def print_report():
    global RESOURCES
    global MONEY
    for item in RESOURCES:
        if item == "water" or item == "milk":
            print(f"{item} : {RESOURCES[item]}ml")
        elif item == "coffee":
            print(f"{item} : {RESOURCES[item]}g")
    print(f"Money: ${MONEY}")
def checking_resources(d_c):
    global MENU
    global RESOURCES
    r = RESOURCES
    ingts = MENU[d_c]['ingredients']
    cost = MENU[d_c]['cost']
    avail = False
    for i in ingts.keys():
        if r[i] < ingts[i]:
            print(f"Sorry there is not enough {i}")
            break
        elif r[i] > ingts[i]:
            avail = True
    if avail:
        coins(cost,ingts,d_c)

def coins(cost,ingts, d_c):
    global MONEY
    quarter = 0.25
    dime = 0.1
    nickel = 0.05
    penny = 0.01
    quarters = int(input("how many quarters?(0.25$): "))
    dimes = int(input("how many dimes?(0.10$): "))
    nickels =int(input("how many nickles?(0.05$): "))
    pennies = int(input("how many pennies?(0.01$): "))
    balance = (quarter*quarters) + (dime*dimes) + (nickel*nickels) + (penny*pennies)
    change= 0
    if cost > balance:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if balance > cost:
            change = round(balance - cost,2)
            print(f"Here is ${change} in change.")
        MONEY += cost
        making_drink(ingts, d_c)

        
def making_drink(ingts, d_c):
    global RESOURCES
    for y in ingts.keys():
        RESOURCES[y] -= ingts[y]
    print(f"Here is your {d_c} ☕. Enjoy!")
Maintenance = False
for item in MENU.keys():
    print(f"{item}: {MENU[item]['cost']}$")
while not Maintenance:

    drink_choice = input("Type 'off' to exit the program, What would you like? (espresso/latte/cappuccino): ").lower()
    if drink_choice == "off":
        print("The Coffee Machine is being turned off for Maintenance.")
        Maintenance = True
    elif drink_choice == "report":
        print_report()
    elif drink_choice in MENU.keys():
        checking_resources(d_c = drink_choice)
    else:
        print("Wrong input!")