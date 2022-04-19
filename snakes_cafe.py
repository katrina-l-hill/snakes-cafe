intro = """
**************************************
** Welcome to the Snakes Cafe! **
** Please see our menu below. **

** To quit at any time, type "quit" **
**************************************
"""



appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

# start program
print(intro)



print("**Appetizers**")
#for x in range(len(appetizers)):
#    print(appetizers[x])

for appetizer in appetizers:
    print(appetizer)

print("**Entrees**")
#for x in range(len(entrees)):
#    print(entrees[x])

for entree in entrees:
    print(entree)

    print("**Desserts**")
#for x in range(len(desserts)):
#    print(desserts[x])

for dessert in desserts:
    print(dessert)

    print("**Drinks**")
#for x in range(len(drinks)):
#    print(drinks[x])

for drink in drinks:
    print(drink)

to_order = """
***********************************
** What would you like to order? **
***********************************
"""

print(to_order)

while True:
    to_order = input('> ')
    if to_order == 'quit':
        break
    print('** 1 order of ', to_order, ' has been added to your meal **')
   