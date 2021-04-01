#def greeting(name):
  # print('hello',name) 

#main program
#input_name= input('enter your name:\n')
#greeting(input_name)

def get order(menu):
    orders = []
    order = input("what would you like to order? (Q to Quit)")

    while (order.uppe() !='Q'):
        #find the order
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("menu item doesn't exist")

        order = input("Anything else? (Q to Quit)")

    return orders