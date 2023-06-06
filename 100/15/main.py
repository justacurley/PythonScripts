
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 100,
}

while True:
    resources_instance = resources.copy()
    choice = input("What would you like? (Espresso, Latte, cappuccino):")
    choice=choice.lower()
    if choice == "off":
        break
    elif choice == "report":
        for item,amount in resources.items():
            print("{} ({})".format(item, amount))
    elif choice in ["espresso","latte","cappuccino"]:
        choice_data = MENU[choice]
        for item,val in choice_data["ingredients"].items():
            if (resources[item] - val) < 0:
                print("Sorry, there is not enough {}.".format(item))
                break
            else:
                resources_instance[item] = resources_instance[item] - val
        quarters=input("Enter Quarters: ")
        dimes=input("Enter Dimes: ")
        nickles=input("Enter Nickles: ")
        pennies=input("Enter Pennies: ")
        if quarters == '':
            quarters = 0
        if dimes == '':
            dimes = 0
        if nickles == '':
            nickles = 0
        if pennies == '':
            pennies = 0
        money_inserted = float(quarters)*.25 + float(dimes)*.10 + float(nickles)*.05 + float(pennies)*.01
        if money_inserted < choice_data["cost"]:
            print("You inserted {}, the cost of a {} is {}".format(money_inserted,choice,choice_data["cost"]))
        else:
            money_returned = money_inserted - choice_data["cost"]
            print("Here is your {} and {} in change.".format(choice,money_returned))
            resources_instance["money"] += choice_data["cost"]
            resources = resources_instance
