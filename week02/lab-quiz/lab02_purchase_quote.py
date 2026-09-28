first_item_name = input("Enter First Item Name:")
first_item_quantity = int(input("Enter First Item Quantity:"))
first_item_price = float(input("Enter First Item Price:"))
second_item_name = input("Enter Second Item Name:")
second_item_quantity = int(input("Enter Second Item Quantity:"))
second_item_price = float(input("Enter Second Item Price:"))
delivery_fee = float(input("Enter delivery fee: "))
tax_percentage = float(input("Enter tax percentage: "))
first_item_total = first_item_quantity * first_item_price
second_item_total = second_item_quantity * second_item_price
subtotal = first_item_total + second_item_total
tax = subtotal * tax_percentage / 100
final_total = subtotal + tax + delivery_fee
print("\n--- Purchase Quote ---")
print(f"{first_item_name}: {first_item_total:.2f} TRY")
print(f"{second_item_name}: {second_item_total:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax: {tax:.2f} TRY")
print(f"Delivery: {delivery_fee:.2f} TRY")
print(f"Final total: {final_total:.2f} TRY")
