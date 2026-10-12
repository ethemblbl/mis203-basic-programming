# mis203-basic-programming

# Student Information
- Name: [İbrahim Ethem Bülbül]
- Student Number: [2404109025]
- Department: Management Information Systems
- Course Name: MIS 203 - Basic Programming

# Week01 
AI Usage Note AI Tool Used: Gemini Prompt Used: "Write a simple Python program that asks for a student's name, department, age, and career goal, then prints a formatted student profile." What did you change? I formatted the print output using Python f-strings to ensure the output matches the required assignment layout clearly and added line spacing.

# Week02
AI Tool Used: Gemini
Prompt Used: "öncelikle vs code'da yazacağım ve deneyerek devam edeceğim. bu ödevin mantığını anlayacağım şekilde aşamalarla ödeve yardım et ardından github kısmına geçeceğim"
What did you change?: I learned how to build the logic step by step and fixed an indentation error related to the continue statement to ensure the loop works correctly.
What does break do in your program?: The break command immediately stops the infinite while loop and exits it when the user types 'q', allowing the program to move on to the final average calculations.

# Week03
AI Tool Used: Gemini

Prompt Used: "ödevin mantığını anlamam gerekiyor!", "satılan bilet sayılarını nasıl göreceğim"

What did you change?: Yapay zekadan kodun temel algoritmasını ve döngü mantığını öğrendikten sonra, sayaçların döngü içindeki yerlerini ve VS Code terminalinde yaşadığım hizalama (indentation) sorunlarını düzelterek kodu ödevin istediği formata getirdim.

Tests:

Normal Test:
Input: Name: Zeynep, Age: 20, Day: Weekday, Student: yes
Result: Zeynep: 140.00 TRY (Student)
Boundary (Sınır Yaş) Testi:
Input: Name: Can, Age: 6, Day: weekend, Student: no
Result: Can: 150.00 TRY (Child) (Not: 6 yaş "Free" değil, "Child" kategorisine girer. 250 TL üzerinden %40 indirim uygulanmıştır.)
Invalid Input Testi:
Input: Name: Deniz, Age: 150
Result: Invalid age.
Why does the order of the rules matter?: Python'daki if/elif yapısı, doğru bulduğu ilk koşula girer ve geri kalan koşulları atlar. Eğer Öğrenci kuralını (%30 indirim) Çocuk kuralından (%40 indirim) önce yazsaydık, 10 yaşındaki öğrenci bir müşteri, hakkı olan çocuk indirimini alamadan sadece %30 öğrenci indirimiyle bilet alırdı. Bu yüzden müşterinin faydasına olan ve öncelikli kurallar her zaman en üste yazılmalıdır.

# Week04
## Surprise Mind Reader

AI Tools: Claude. Gemini

A fun Python terminal project that starts with a fake crash prank and ends with a cool mind-reading trick using binary numbers.

##  What is this?

This is a small console project I built with two main parts:

1. **The Fake Crash:** It pretends to run into system errors, shows a fake progress bar deleting `homework.py`, and does a shutdown countdown to scare the user a bit (just text, nothing actually gets deleted!).
2. **The Mind Reader:** It asks the user to pick a number between 1 and 63. After showing 6 different cards and asking if the number is on them, the program guesses the exact number.

##  How does it work?

It's not magic, it's just binary numbers!

- Any number from 1 to 63 can be written in binary using 6 bits: 1, 2, 4, 8, 16, and 32.
- Each card shows numbers that have a specific bit turned on.
- When you answer "yes", the program simply adds the first number of that card (1, 2, 4, 8, 16, or 32) together.
- The cards are shuffled randomly so it feels more like magic.

##  Features

- Typewriter-like text effect (`slow_print`).
- Screen clearing that works on both Windows and Mac/Linux.
- Handles user inputs so only valid answers (`yes` or `no`) work.
- Built only with Python's built-in libraries (`os`, `random`, `time`) — no external packages needed.
