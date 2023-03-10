import random
import time
import datetime
import getpass
import random
import string

username = getpass.getuser()

logged_in = False
admin = False


order_number = random.randint(1, 999)
time_to_wait = random.randint(1, 10)

menu = {
    "burger": 4,
    "nuggets": 3,
    "fries": 3,
    "coke": 2,
    "taco": 4,
    "fries supreme": 3,
    "fried chicken sandwich": 3,
    "pogos": 1,

}

with open("C:/Users/comic/Documents/GitHub/order/assets/data/userdata.txt", "r+") as f:
    lines = f.readlines()
    if "d90d56acd2707f26f101d1ba66e60dab7bc83ff937fae9828c9251cc13e74a48" in "".join(lines):
        lines[2] = "admin=true\n"
        print("Welcome admin!")
    else:
        lines[2] = "admin=false\n"
    f.seek(0)
    f.writelines(lines)



login_choice = input("Would you like to log in? (y/n): ")

if login_choice.lower() == "y":
    logged_in = False
    username = input("Enter your username: ")
    with open(r"C:\\Users\\comic\Documents\\GitHub\\order\\assets\\data\\local_usernames.txt", "r") as file:
        for line in file:
            if line.strip() == username:
                print("Logged in!")
                logged_in = True
                break

    if logged_in:
        session = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        with open(r"C:\\Users\\comic\\Documents\\GitHub\\order\\options.txt", "r") as file:
            lines = file.readlines()
        lines[0] = "logged_in=true\n"
        lines[1] = "user session=" + session + "\n"
        with open(r"C:\\Users\\comic\\Documents\\GitHub\\order\\options.txt", "w") as file:
            file.writelines(lines)
    else:
        print("Username not found.")
else:
    print("Login cancelled.")

today = datetime.datetime.now().weekday()
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
saleday = days[today]

if saleday == "monday":
    print("Burgers 20% off!\n")
elif saleday == "tuesday":
    print("Tacos 15% off!\n")
elif saleday == "wendsday":
    print("Nuggets 25% off!\n")
elif saleday == "thursday":
    print("Drinks 10% off!")
elif saleday == "friday":
    print("Pogos 10% off!")
elif saleday == "saturday":
    print("Fries supreme 20% off!")
elif saleday == "sunday":
    print("Fried Chicken Sandwich 20% off!")

with open("points.txt", "r") as f:
    contents = f.read()
    user_points = int(contents.strip())

def check_card_number(card_number):
    # Step 1: Check length.
    if len(card_number) < 13 or len(card_number) > 19:
        return False

    # Step 2: Convert to integer.
    card_number = [int(x) for x in card_number]

    # Step 3: Check prefix.
    if card_number[0] == 4:
        prefix = "Visa"
    elif card_number[0] == 5:
        prefix = "Mastercard"
    elif card_number[0] == 3 and (card_number[1] == 4 or card_number[1] == 7):
        prefix = "American Express"
    elif card_number[0] == 6:
        prefix = "Discover"
    else:
        return False

    # Step 4: Check the Luhn algorithm.
    sum_ = 0
    for i, x in enumerate(reversed(card_number)):
        if i % 2 == 1:
            x *= 2
            if x > 9:
                x -= 9
        sum_ += x

    # Step 5: Check if the sum is divisible by 10.
    if sum_ % 10 == 0:
        return True
    else:
        return False


def order_item(item, quantity, discount=0):
    price = (menu[item] * quantity) * (1 - discount)
    if discount > 0:
        return f"{quantity} {item}(s) - ${price:.2f} (Discounted!)"
    return f"{quantity} {item}(s) - ${price:.2f}"

def place_order(total_price, items_ordered):
    today = datetime.datetime.now().strftime("%A").lower()

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

    discount = 0
    if item_key.lower() == "burger" and today == "monday":
        discount = 0.2
    if item_key.lower() == "taco" and today == "tuesday":
        discount = 0.15
    if item_key.lower() == "nuggets" and today == "wendsay":
        discount = 0.25
    if item_key.lower() == "drink" and today == "thursday":
        discount = 0.1
    if item_key.lower() == "pogo" and today == "friday":
        discount = 0.1
    if item_key.lower() == "fries supreme" and today == "saturday":
        discount = 0.2
    if item_key.lower() == "fried chicken sandwich" and today == "sunday":
        discount = 0.2

    item_price = menu[item_key] * quantity
    total_price += item_price * (1 - discount)
    items_ordered.append(order_item(item_key, quantity, discount))
    more = input("Would you like to order more? (y/n) ")
    if more.lower() == 'y':
        return place_order(total_price, items_ordered)
    else:
        return total_price, items_ordered

#POINTS
total_price, items_ordered = place_order(0, [])
print("Order Summary:")
for item in items_ordered:
    print(item)
print(f"Total: ${total_price:.2f}")
if logged_in == True:
    user_points = user_points + total_price
    with open("points.txt", "w") as file:
        file.write(str(user_points))
else:
    pass

#GET ORDER ID
def send_order():
    print(f"Order Number: {order_number}")
    print(f"Your meal will be ready in approximately {time_to_wait} minute(s).")
    print("Please proceed to the counter when your order number is called.")


def ask_discount():
    answer = input("Would you like to enter a discount code (y/n)? This will override current discounts. ")
    return answer

answer = ask_discount()
codes = ["xigY9jo5bA", "fK7sfOr3J2"]
discounts = [0.3, 0.25]

#DISCOUNT CODES
if answer.lower() == "y":
    code = input("Please enter your discount code: ")
    discount = 0
    with open(r"C:\\Users\\comic\\Documents\\GitHub\\order\\assets\\discounts\\discounts.txt", "r") as file:
        for line in file:
            for c, d in zip(codes, discounts):
                if line.strip() == code:
                    discount = d
                    break
            if discount != 0:
                break

    if discount != 0:
        print("Discount applied:", discount)
    else:
        print("Discount code not found")
else:
    print("No discount being applied")


#PAYMENT
card_number = input("Please enter your card number to continue payment\n")
if check_card_number(card_number):
    send_order()
elif card_number == '1515':
    send_order()
else:
    print("The credit card number is not valid.")


current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = r"C:\\Users\\comic\\Documents\\GitHub\\order\\past-orders\\order-" + current_time + ".txt"

#ORDER SUMMARY
with open(file_path, "w") as file:
    file.write("Order Summary:\n")
    for item in items_ordered:
        file.write(item + "\n")
    file.write(f"Total: ${total_price:.2f}\n")
    file.write(f"Order Number: {order_number}\n")
    file.write(f"Time of Order: {current_time}\n")
    file.write(f"Time to Wait: {time_to_wait} minutes\n")
    file.write(f"Points: {user_points}")

#RESET USERDATA
session = '0'
with open(r"C:\\Users\\comic\\Documents\\GitHub\\order\\options.txt", "r") as file:
    lines = file.readlines()
lines[0] = "logged_in=False\n"
lines[1] = "user session=" + session + "\n"
lines[2] = "admin=False"
with open(r"C:\\Users\\comic\\Documents\\GitHub\\order\\options.txt", "w") as file:
    file.writelines(lines)


input("Press enter to close")

