# Card reader used when paying.

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

# Example usage
card_number = input("Enter the credit card number: ")
if check_card_number(card_number):
    print("The credit card number is valid.")
else:
    print("The credit card number is not valid.")
