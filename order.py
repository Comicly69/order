import random
import time
import datetime

menu = {
    "burger": 3.99,
    "quarter pounder": 4.99,
    "nuggets": 4.49,
    "fries": 2.49,
    "drink": 1.99
}

def order_item(item, quantity):
    price = menu[item] * quantity
    return f"{quantity} {item}(s) - ${price:.2f}"

def place_order(total_price, items_ordered):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

    item = input("\nWhat would you like to order?\n ")
    if item.lower() not in menu:
        print(f"{item} is not on the menu.")
        return place_order(total_price, items_ordered)
    item_key = next((key for key, value in menu.items() if item.lower() == key), None)
    quantity = input("How many would you like to order? ")
    try:
        quantity = int(quantity)
    except ValueError:
        print("Invalid quantity. Please try again.")
        return place_order(total_price, items_ordered)
    item_price = menu[item_key] * quantity
    total_price += item_price
    items_ordered.append(order_item(item_key, quantity))
    more = input("Would you like to order more? (y/n) ")
    if more.lower() == 'y':
        return place_order(total_price, items_ordered)
    else:
        return total_price, items_ordered

total_price, items_ordered = place_order(0, [])
print("Order Summary:")
for item in items_ordered:
    print(item)
print(f"Total: ${total_price:.2f}")

order_number = random.randint(1, 999)
time_to_wait = random.randint(1, 10)
print(f"Order Number: {order_number}")
print(f"Your meal will be ready in approximately {time_to_wait} minutes.")
print("Please proceed to the counter when your order number is called.")

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = r"C:\Users\comic\Documents\GitHub\order\past-orders\order-" + current_time + ".txt"

with open(file_path, "w") as file:
    file.write("Order Summary:\n")
    for item in items_ordered:
        file.write(item + "\n")
    file.write(f"Total: ${total_price:.2f}\n")
    file.write(f"Order Number: {order_number}\n")
    file.write(f"Time of Order: {current_time}\n")
    file.write(f"Time to Wait: {time_to_wait} minutes")

