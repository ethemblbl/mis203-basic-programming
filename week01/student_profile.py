# Kullanıcıdan bilgileri alıyoruz (input fonksiyonu metin olarak okur)
name = input("Enter your name: ")
department = input("Enter your department: ")
age = input("Enter your age: ")
career_goal = input("Enter your career goal: ")

# Bilgileri ekrana formatlı bir şekilde yazdırıyoruz
print("\n--- Student Profile ---")
print(f"Name: {name}")
print(f"Department: {department}")
print(f"Age: {age}")
print(f"Career Goal: {career_goal}")
