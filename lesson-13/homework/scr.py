from datetime import datetime, timedelta
import time
import re
import pytz

def meeting_scheduler():
    current_str = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Uchrashuv davomiyligi (soat): "))
    duration_minutes = int(input("Qo‘shimcha daqiqa: "))
    current_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    end_time = current_time + timedelta(hours=duration_hours, minutes=duration_minutes)
    print(f" Uchrashuv tugash vaqti: {end_time}")

 
def timezone_converter():
    dt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
    from_tz = input("Hozirgi timezone (masalan: Asia/Tashkent): ")
    to_tz = input("O‘zgartirmoqchi bo‘lgan timezone (masalan: Europe/London): ")
    naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    local_dt = from_zone.localize(naive_dt)
    converted_dt = local_dt.astimezone(to_zone)
    print(f" O‘zgartirilgan vaqt: {converted_dt}")
def countdown_timer():
    future_str = input("Kelajakdagi vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
    future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")
    print(" Tayyor... Sanash boshlandi:")
    while True:
        now = datetime.now()
        diff = future - now
        if diff.total_seconds() <= 0:
            print(" Vaqt tugadi!")
            break
        print(f"Qolgan vaqt: {diff}", end="\r")
        time.sleep(1)

def email_validator():
    email = input("Email manzilni kiriting: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print(" To‘g‘ri email manzil.")
    else:
        print(" Email manzil noto‘g‘ri.")

 
def phone_formatter():
    number = input("Telefon raqamni kiriting (faqat raqamlar bilan): ")
    if len(number) == 10:
        formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
        print(" Formatlangan raqam:", formatted)
    else:
        print(" Raqam uzunligi noto‘g‘ri (10 ta raqam bo‘lishi kerak).")

 
def password_checker():
    password = input("Parol kiriting: ")
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    if all([length, upper, lower, digit]):
        print(" Kuchli parol!")
    elif length and (upper or lower) and digit:
        print(" O‘rta darajadagi parol.")
    else:
        print(" Zaif parol. Harflar va raqamlar aralash bo‘lishi kerak.")

 
def word_finder():
    text = """Python is great. Python is powerful. I love Python programming."""
    word = input("Qidiriladigan so‘zni kiriting: ")
    count = text.lower().count(word.lower())
    print(f"🔍 '{word}' so‘zi matnda {count} marta uchradi.")

 
def date_extractor():
    text = input("Matn kiriting (ichida sanalar bo‘lishi mumkin): ")
    pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b'
    dates = re.findall(pattern, text)
    if dates:
        print(" Topilgan sanalar:", dates)
    else:
        print(" Sana topilmadi.")

 
def main():
    while True:
        print("\n===== 🧠 MULTI TASK PYTHON PROGRAM =====")
        print("1. Meeting Scheduler")
        print("2. Timezone Converter")
        print("3. Countdown Timer")
        print("4. Email Validator")
        print("5. Phone Number Formatter")
        print("6. Password Strength Checker")
        print("7. Word Finder")
        print("8. Date Extractor")
        print("0. Chiqish")

        choice = input("Tanlang (0-8): ")

        if choice == "1":
            meeting_scheduler()
        elif choice == "2":
            timezone_converter()
        elif choice == "3":
            countdown_timer()
        elif choice == "4":
            email_validator()
        elif choice == "5":
            phone_formatter()
        elif choice == "6":
            password_checker()
        elif choice == "7":
            word_finder()
        elif choice == "8":
            date_extractor()
        elif choice == "0":
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov. 0 dan 8 gacha kiriting!")

 
if __name__ == "__main__":
    main()

