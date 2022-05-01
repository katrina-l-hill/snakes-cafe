# variable to hold order info
order = {}

intro = """
**************************************
** Welcome to the Snakes Cafe! **
** Please see our menu below. **
**
** To quit at any time, type "quit" **
**************************************
"""


appetizers = ["Wings", "Cookies", "Spring Rolls"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]

all_menu_items = appetizers + entrees + desserts + drinks

# start program
print(intro)


print("Appetizers")
print("---------")
# for x in range(len(appetizers)):
#    print(appetizers[x])

for appetizer in appetizers:
    print(appetizer)

print()
print("Entrees")
print("---------")
# for x in range(len(entrees)):
#    print(entrees[x])

for entree in entrees:
    print(entree)

print()
print("Desserts")
print("---------")
# for x in range(len(desserts)):
#    print(desserts[x])

for dessert in desserts:
    print(dessert)

print()
print("Drinks")
print("---------")
# for x in range(len(drinks)):
#    print(drinks[x])

for drink in drinks:
    print(drink)

prompt = """
***********************************
** What would you like to order? **
***********************************
"""

print(prompt)


def print_order():
    for item in order.keys():
        if order[item] > 1:
            print(f"** {order[item]} orders of {item} have been added to your meal **")
        else:
            print(f"** {order[item]} order of {item} has been added to your meal **")


while True:
    response = input("> ")
    if response == "quit":
        # print quit message
        quit()
    elif response in all_menu_items:
        # add to order
        if response in order.keys():
            # if item is already in dictionary, increment it
            order[response] += 1
        else:
            # add item to dictionary and set to 1
            order[response] = 1
        # show order
        print_order()
    else:
        # show custom error message
        print(f"Unfortunately, {response} is not offered on our menu.")
