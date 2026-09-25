total_students = 0
total_score = 0  

while True: # DÖNGÜ BAŞLIYOR (Bunun altındaki her şey içeride olmalı)
    name = input("Enter student name (or q to quit): ")
    
    if name == 'q':
        break
        
    score = float(input("Enter score: "))
    
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue  # BURASI: "if" ile aynı içerilikte, while'a göre 2 sekme içeride olmalı.

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade ="F"

    #sonucu ödevin istediği gibi ekrana yazdırıyoruz.
    print(f"{name}: {int(score)} -> {grade}")


if total_students == 0:
    print("No students entered.")
else:
    average = total_score / total_students
    print(f"Total students: {total_students}")
    print(f"Average score: {average: .2f}") #2f kısmı virgülden sonra iki basamak gösterir. 
    
