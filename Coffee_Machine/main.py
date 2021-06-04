import sys

MENU = {
    "expresso": {
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
}

menuItems = {
"expresso": True,
"latte": True,
"cappuccino": True,
"Off": True,
"repor": True

}

Earnings = {
    "Money": 0
}
def userInput():
    
    try:
        order= str(input("What would you like (expresso, latte,cappuccino)? "))
        order=order.lower()
    except:
        print("Please enter single quotes around the input value '' ?")
        quit()
    try:
        menuItems[order]
        haveDrink=True
    except:
        print("I am sorry, we currently don't offer the requested product. \n Have a great day!")
        haveDrink=False
    if order == "Off":
        print("Program is shutting off")
        quit()
    if order == "report":
        printReport()
    return order, haveDrink

def printReport():
    print("Water", resources["water"])
    print("milk", resources["milk"])
    print("coffee", resources["coffee"])
    print("EarnedAmount", Earnings["Money"])

def makeOrder(item):

    if item == "expresso":
        resources["water"] = resources["water"] - MENU["expresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["expresso"]["ingredients"]["coffee"]
    if item == "latte":
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]

    if item == "cappuccino":
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]

def checkResources(item):

    try:
        if resources["water"] < MENU[item]["ingredients"]["water"]:
            print("Sorry we don't have enough resources.")
            return False    
        
        if resources["milk"] < MENU[item]["ingredients"]["milk"]:
            print("Sorry we don't have enough resources.")
            return False 

        if resources["coffee"] < MENU[item]["ingredients"]["coffee"]:
            print("Sorry we don't have enough resources.")
            return False
    except:
        pass 

def getMoney(item):
    money=float(input("Please Enter the Coin. (Please note you can only put upto Quarter $0.25): "))
    if money == MENU[item]["cost"]:
        Earnings["Money"] = MENU[item]["cost"]
        print("Thank you for your business!")
    if money > MENU[item]["cost"]:
        Earnings["Money"] = MENU[item]["cost"]
        print("Here is your change: ", MENU[item]["cost"])
        print("Thank you for your business!")
    if money < MENU[item]["cost"]:
        
        print("Sorry you don't have sufficient money. ")
        print("Thank you for your business!")

def run():
    i = 0
    while i < 10:
        item,haveDrink=userInput()
        if item != "report" and haveDrink == True:
            isEnoughResources=checkResources(item)
            if isEnoughResources != False:
                makeOrder(item)
                getMoney(item)
                i += 1


if __name__ == "__main__":
    run()