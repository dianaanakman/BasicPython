orders=[]
order = input("what would you like to order ? (Q to Quit)")

while(order.upper() !='Q'):
    found = menu.get(order)
if found:
    orders.append(order)
else:
    print("Menu item doesn't exist")

order = input("Anything else? (Q to Quit)")

    print(orders)