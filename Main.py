from menu import MENU
from menu import resources

money = 0
should_continue = True

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

def print_report():
        print("Water:", resources["water"], "ml")
        print("Milk:", resources["milk"], "ml")
        print("Coffee:", resources["coffee"], "g")
        print(f"Money: ${money}")

def coffee_maker(coffee_choice):

    if coffee_choice == "espresso":
        water_needed = MENU["espresso"]["ingredients"]["water"]
        coffee_needed = MENU["espresso"]["ingredients"]["coffee"]
        cost = MENU["espresso"]["cost"]

        if water_needed > resources["water"]:
            print("The Machine has not enough water.")
            return False
        if coffee_needed > resources["coffee"]:
            print("The Machine has not enough coffee.")
            return False

        resources["water"] -= water_needed
        resources["coffee"] -= coffee_needed



    elif coffee_choice == "latte":
        water_needed = MENU["latte"]["ingredients"]["water"]
        coffee_needed = MENU["latte"]["ingredients"]["coffee"]
        milk_need = MENU["latte"]["ingredients"]["milk"]
        cost = MENU["latte"]["cost"]

        if water_needed > resources["water"]:
            print("The Machine has not enough water.")
            return False
        if coffee_needed > resources["coffee"]:
            print("The Machine has not enough coffee.")
            return False
        if milk_need > resources["milk"]:
            print("The Machine has not enough milk.")
            return False

        resources["water"] -= water_needed
        resources["coffee"] -= coffee_needed
        resources["milk"] -= milk_need


    elif coffee_choice == "cappuccino":
        water_needed = MENU["cappuccino"]["ingredients"]["water"]
        coffee_needed = MENU["cappuccino"]["ingredients"]["coffee"]
        milk_need = MENU["cappuccino"]["ingredients"]["milk"]
        cost = MENU["cappuccino"]["cost"]

        if water_needed > resources["water"]:
            print("The Machine has not enough water.")
            return False
        if coffee_needed > resources["coffee"]:
            print("The Machine has not enough coffee.")
            return False
        if milk_need > resources["milk"]:
            print("The Machine has not enough milk.")
            return False


        resources["water"] -= water_needed
        resources["coffee"] -= coffee_needed
        resources["milk"] -= milk_need


    print(f"You have chosen a {coffee_choice}.")
    return True

def monetary_options(choice):
    global money
    qtd_quarters = float(input("How many quarters: "))
    qtd_dimes = float(input("How many dimes: "))
    qtd_nickles = float(input("How many nickles: "))
    qtd_pennies = float(input("How many pennies: "))

    total_quarters = qtd_quarters * quarters
    total_dimes = qtd_dimes * dimes
    total_nickles = qtd_nickles * nickles
    total_pennies = qtd_pennies * pennies

    total_money = total_quarters + total_dimes + total_nickles + total_pennies

    print(f"You inserted: ${total_money}")



    if total_money >= MENU[coffee_choice]["cost"]:
        money += MENU[coffee_choice]["cost"]
        change = round(total_money - MENU[coffee_choice]["cost"], 2)
        if change > 0:
            print(f"Your total change is ${change}")
        return True
    else:
        print("You don't have enough money. Money refunded.")
        return False




while should_continue:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == "off":
        print("Turning off the machine.")
        should_continue = False
        continue
    if coffee_choice == "report":
        print_report()
        continue
    if coffee_choice not in MENU:
        print("Invalid choice.Please choose again.")
        continue

    if coffee_choice in MENU:
        if coffee_maker(coffee_choice):
            monetary_options(coffee_choice)
    print(f"Total money in machine: {money}")






