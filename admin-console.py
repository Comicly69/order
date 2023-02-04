import ccard
import uuid

with open("C:/Users/comic/Documents/GitHub/order/assets/data/userdata.txt", "r+") as f:
    lines = f.readlines()
    if "d90d56acd2707f26f101d1ba66e60dab7bc83ff937fae9828c9251cc13e74a48" in "".join(lines):
        pass
    else:
        exit()

def get_hwid():
    print (str(uuid.getnode()))



def card(card_type):
    if card_type == "visa":
        print(ccard.visa())
    elif card_type == "mastercard":
        print(ccard.mastercard())
    elif card_type == "discover":
        print(ccard.discover())
    elif card_type == "amex":
        print(ccard.amex())

menu = {
    "gencard.visa": lambda: card("visa"),
    "gencard.mastercard": lambda: card("mastercard"),
    "gencard.discover": lambda: card("discover"),
    "gencard.amex": lambda: card("amex")
}

print("Welcome to admin utilities, this is a collection of tools to assist you!")

while True:
    command = input("Please type a command to continue, if you need a list of available commands, type 'help'\n ")

    if command == "help":
        print("gencard.visa: Generate a visa credit card")
        print("gencard.mastercard: Generate a mastercard credit card")
        print("gencard.discover: Generate a discover credit card")
        print("gencard.amex: Generate a amex credit card")
        print("tell user all uses of commands")
        print("exit: exit the program")
    elif command == "gethwid":
        get_hwid()
    elif command in menu:
        menu[command]()
    elif command == "exit":
        break
    else:
        print("Invalid command, please try again.")
