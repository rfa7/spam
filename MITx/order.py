order = "salad water hamburger salad hamburger"
def item_order(order):
    salad = 0
    hamburger = 0
    water = 0

    for i in order.split():
        if i == 'salad':
            salad += 1
        elif i == 'hamburger':
            hamburger += 1
        elif i == 'water':
            water += 1
    return 'salad:' + str(salad) + ' hamburger:' + str(hamburger) + ' water:' + str(water)
print item_order(order)
