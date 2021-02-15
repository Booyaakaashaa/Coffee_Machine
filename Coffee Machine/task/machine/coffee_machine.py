# Write your code here

def buy(water, milk, coffee_beans, cups, money ):
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if choice == "back":
        return water, milk, coffee_beans, cups, money
    if choice == "1":
        if water >= 250:
            water -= 250
        else:
            print("Sorry, not enough water!\n")
            return water, milk, coffee_beans, cups, money
        if coffee_beans >= 16:
            coffee_beans -= 16
        else:
            water += 250
            print("Sorry, not enough coffee beans!\n")
            return water, milk, coffee_beans, cups, money
        money += 4
        if cups >= 1:
            cups -= 1
        else:
            water += 250
            coffee_beans += 16
            print("Sorry, not enough cups!\n")
            return water, milk, coffee_beans, cups, money
    elif choice == "2":
        if water >= 350:
            water -= 350
        else:
            print("Sorry, not enough water!\n")
            return water, milk, coffee_beans, cups, money
        if coffee_beans >= 20:
            coffee_beans -= 20
        else:
            water += 350
            print("Sorry, not enough coffee beans!\n")
            return water, milk, coffee_beans, cups, money
        money += 7
        if cups >= 1:
            cups -= 1
        else:
            water += 350
            coffee_beans += 20
            print("Sorry, not enough cups!\n")
            return water, milk, coffee_beans, cups, money
        if milk >= 75:
            milk -= 75
        else:
            water += 350
            coffee_beans += 20
            cups += 1
            print("Sorry, not enough milk!\n")
            return water, milk, coffee_beans, cups, money
    elif choice == "3":
        if water >= 200:
            water -= 200
        else:
            print("Sorry, not enough water!\n")
            return water, milk, coffee_beans, cups, money
        if coffee_beans >= 12:
            coffee_beans -= 12
        else:
            water += 200
            print("Sorry, not enough coffee beans!\n")
            return water, milk, coffee_beans, cups, money
        money += 6
        if cups >= 1:
            cups -= 1
        else:
            water += 200
            coffee_beans += 12
            print("Sorry, not enough cups!\n")
            return water, milk, coffee_beans, cups, money
        if milk >= 100:
            milk -= 100
        else:
            water += 200
            coffee_beans += 12
            cups += 1
            print("Sorry, not enough milk!\n")
            return water, milk, coffee_beans, cups, money
    print("I have enough resources, making you a coffee!\n")
    return water, milk, coffee_beans, cups, money


def fill(water, milk, coffee_beans, cups, money):
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    return water, milk, coffee_beans, cups, money

# def take():


def state_print(w, mi, cb, c, mo):
    out = """The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money""".format(w, mi, cb, c, mo)
    print(out)


def main():
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550

    while 1:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            water, milk, coffee_beans, cups, money = buy(water, milk, coffee_beans, cups, money)
        elif action == "fill":
            water, milk, coffee_beans, cups, money = fill(water, milk, coffee_beans, cups, money)
        elif action == "take":
            print("I gave you $550")
            money = 0
        elif action == "remaining":
            print()
            state_print(water, milk, coffee_beans, cups, money)
        else:
            break


if __name__ == '__main__':
    main()


"""water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups = int(input("Write how many cups of coffee you will need:\n"))

store = min(water // 200, milk // 50, coffee // 15)

if store > cups:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(store - cups))
elif store == cups:
    print("Yes, I can make that amount of coffee")
else:
    if store == 1:
        print("No, I can make only 1 cup of coffee")
    else:
        print("No, I can make only {} cups of coffee".format(store))
"""
