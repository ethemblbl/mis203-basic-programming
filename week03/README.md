## Week 03

**AI Tool Used:** Gemini

**Prompt Used:** "ödevin mantığını anlamam gerekiyor!", "satılan bilet sayılarını nasıl göreceğim"

**What did you change?:**
Yapay zekadan kodun temel algoritmasını ve döngü mantığını öğrendikten sonra, sayaçların döngü içindeki yerlerini ve VS Code terminalinde yaşadığım hizalama (indentation) sorunlarını düzelterek kodu ödevin istediği formata getirdim.

**Tests:**

1. **Normal Test:**
* Input: Name: Zeynep, Age: 20, Day: Weekday, Student: yes
* Result: Zeynep: 140.00 TRY (Student)


2. **Boundary (Sınır Yaş) Testi:**
* Input: Name: Can, Age: 6, Day: weekend, Student: no
* Result: Can: 150.00 TRY (Child) (Not: 6 yaş "Free" değil, "Child" kategorisine girer. 250 TL üzerinden %40 indirim uygulanmıştır.)


3. **Invalid Input Testi:**
* Input: Name: Deniz, Age: 150
* Result: Invalid age.


**Why does the order of the rules matter?:**
Python'daki if/elif yapısı, doğru bulduğu ilk koşula girer ve geri kalan koşulları atlar.
Eğer Öğrenci kuralını (%30 indirim) Çocuk kuralından (%40 indirim) önce yazsaydık, 10 yaşındaki öğrenci bir müşteri, hakkı olan çocuk indirimini alamadan sadece %30 öğrenci indirimiyle bilet alırdı. 
Bu yüzden müşterinin faydasına olan ve öncelikli kurallar her zaman en üste yazılmalıdır.
