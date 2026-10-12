# lab03_order_approval.py


def main():
  # 1. Girdilerin alınması
  try:
    order_amount = float(input("Enter order amount (TRY): "))
    available_stock = int(input("Enter available stock: "))
    requested_quantity = int(input("Enter requested quantity: "))
    membership_input = (
        input("Is the customer a member? (yes/no): ").strip().lower()
    )
  except ValueError:
    print("Order Rejected: Invalid input format. Please enter numeric values.")
    return

  is_member = membership_input in ["yes", "y", "true"]

  # 2. Red Kontrolleri (Geçersiz miktar veya yetersiz stok)
  # Not: Red durumunda kesinlikle son fiyat gösterilmez.
  if requested_quantity <= 0:
    print("Order Rejected: Requested quantity must be greater than zero.")
  elif requested_quantity > available_stock:
    print(
        f"Order Rejected: Insufficient stock. (Requested: {requested_quantity},"
        f" Available: {available_stock})"
    )

  # 3. Onay ve Fiyatlandırma Kontrolleri
  else:
    # Mantıksal operatör (and) kullanımı
    if is_member and order_amount >= 500:
      discount = order_amount * 0.10
      final_price = order_amount - discount
      approval_reason = (
          "Stock verified. Member discount of 10% applied (order >= 500 TRY)."
      )
    elif is_member and order_amount < 500:
      final_price = order_amount
      approval_reason = (
          "Stock verified. Member discount not applied (order is below 500"
          " TRY)."
      )
    else:
      final_price = order_amount
      approval_reason = "Stock verified. Standard non-member pricing applied."

    # Onaylanan siparişte gerekçe ve nihai fiyat gösterilir
    print("Order Approved!")
    print(f"Reason: {approval_reason}")
    print(f"Final Price: {final_price:.2f} TRY")


if __name__ == "__main__":
  main()
