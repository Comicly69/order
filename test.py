discount = 0
codes = ["xigY9jo5bA", "fK7sfOr3J2"]
discounts = [0.3, 0.25]

answer = input("Would you like to enter a discount code (y/n)? ")

if answer.lower() == "y":
    code = input("Please enter your discount code: ")
    with open("C:\\Users\\comic\\Documents\\GitHub\\order\\assets\\discounts\\discounts.txt", "r") as file:
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

# Placeholder for sending order
print("Sending order")