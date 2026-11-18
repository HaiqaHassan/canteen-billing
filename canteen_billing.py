
print("===== CAMPUS CANTEEN BILLING SYSTEM =====")

subtotal = 0
total_quantity = 0

while True:
    print("\n----- MENU -----")
    print("1. Tea      - PKR 80")
    print("2. Sandwich - PKR 250")
    print("3. Juice    - PKR 150")
    print("4. Coffee   - PKR 180")
    print("0. Checkout")

    choice = input("Select an item (0 to checkout): ")

    if choice == "0":
        break
    elif choice == "1":
        item = "Tea"
        price = 80
    elif choice == "2":
        item = "Sandwich"
        price = 250
    elif choice == "3":
        item = "Juice"
        price = 150
    elif choice == "4":
        item = "Coffee"
        price = 180
    else:
        print("Invalid choice! Please try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    item_total = price * quantity
    subtotal = subtotal + item_total
    total_quantity = total_quantity + quantity

    print(item, "added successfully!")
    print("Item total: PKR", item_total)

print("\n===== FINAL BILL =====")
print("Total quantity:", total_quantity)
print("Subtotal: PKR", subtotal)

if subtotal >= 1000:
    discount = subtotal * 10 / 100
else:
    discount = 0

final_bill = subtotal - discount

print("Discount: PKR", discount)
print("Final bill: PKR", final_bill)
print("Thank you for visiting!")
