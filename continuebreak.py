#
# shoppinglist = ["Milk" , "pasta" , "bread" , "Jam" , "Wheat flour"]
#
# for item in shoppinglist:
#     if ( item == 'bread'):
#         break
#     print("Buy " + item)

meal = ["egg", "bacon", "ketchup", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
# The else defined below is used if the loop executes without break, then the else block is executed
else:
    print("I'll have a plate of that then")

if nasty_food_item:
    print('Can\'t I have anything without having spam in it')

