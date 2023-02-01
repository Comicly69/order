menu = {
    "Big Mac": 3.99,
    "Quarter Pounder": 4.99,
    "Chicken McNuggets": 4.49,
    "French Fries": 2.49,
    "Coca Cola": 1.99
}

def order_item(item, quantity):
    price = menu[item] * quantity
    return f"You ordered {quantity} of {item} for a total of ${price:.2f}"

item = input("What would you like to order? ")
quantity = int(input("How many would you like to order? "))

print(order_item(item, quantity))
