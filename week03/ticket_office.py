# 1. Sayaçlar döngünün dışında (en üstte) tanımlanır
tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

# 2. Ana döngü başlar
while True:
    # İsim alma ve çıkış kontrolü
    name = input("Customer name (or q to quit): ")
    if name.lower() == 'q':
        break
        
    # Yaş bilgisi alma ve doğrulama
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age.")
        continue
        
    # Gün bilgisi alma ve doğrulama
    day = input("Day (weekday/weekend): ").lower()
    if day != "weekday" and day != "weekend":
        print("Invalid day.")
        continue
        
    # Öğrenci durumu alma ve doğrulama
    student_input = input("Student (yes/no): ").lower()
    if student_input != "yes" and student_input != "no":
        print("Please answer yes or no.")
        continue
        
    is_student = (student_input == "yes")
    
    # 3. Taban fiyatı belirleme
    if day == "weekday":
        base_price = 200
    else:
        base_price = 250
        
    # 4. İndirimleri sırasıyla kontrol etme
    if age < 6:
        ticket_type = "Free"
        discount = 1.0
    elif age >= 65:
        ticket_type = "Senior"
        discount = 0.50
    elif age >= 6 and age <= 12: 
        ticket_type = "Child"
        discount = 0.40
    elif is_student and age <= 25:
        ticket_type = "Student"
        discount = 0.30
    else:
        ticket_type = "Standard"
        discount = 0.0
        
    # Son fiyatı hesaplama
    final_price = base_price * (1 - discount)
    
    # O müşterinin fişini yazdırma
    print(f"{name}: {final_price:.2f} TRY ({ticket_type})")
    
    # 5. İstatistikleri (sayaçları) güncelleme
    tickets_sold += 1
    total_revenue += final_price
    if ticket_type == "Free":
        free_tickets += 1

# 6. DÖNGÜ DIŞI - Özet Ekranı (Girintiler tamamen en sola yaslı)
if tickets_sold == 0:
    print("No tickets sold.")
else:
    average_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {average_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
