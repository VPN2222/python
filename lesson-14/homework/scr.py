{
    "students": [
        {
            "name": "Alice",
            "age": 20,
            "grade": "A"
        },
        {
            "name": "Bob",
            "age": 22,
            "grade": "B"
        },
        {
            "name": "Charlie",
            "age": 19,
            "grade": "A+"
        }
    ]
}

import json
 
with open('students.json', 'r') as file:
    data = json.load(file)
 
for student in data['students']:
    print("Name:", student['name'])
    print("Age:", student['age'])
    print("Grade:", student['grade'])
    print("-" * 30)

import requests
 
API_KEY = "YOUR_API_KEY"
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

 
response = requests.get(URL)
data = response.json()

 
if response.status_code == 200:
    print(" Shahar:", data['name'])
    print(" Harorat:", data['main']['temp'], "°C")
    print(" Namlik:", data['main']['humidity'], "%")
    print(" Shamol tezligi:", data['wind']['speed'], "m/s")
    print(" Tavsif:", data['weather'][0]['description'])
else:
    print("Xatolik:", data['message'])
import json
import os

FILENAME = 'books.json'
 
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as f:
        json.dump({"books": []}, f, indent=4)
 
def load_books():
    with open(FILENAME, 'r') as f:
        return json.load(f)
 
def save_books(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=4)
 
def add_book():
    data = load_books()
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = input("Yil: ")
    
    new_book = {"title": title, "author": author, "year": year}
    data["books"].append(new_book)
    save_books(data)
    print(" Kitob qoshildi!")

def update_book():
    data = load_books()
    title = input("Qaysi kitobni yangilaysiz (nomi): ")

    for book in data["books"]:
        if book["title"].lower() == title.lower():
            print("Topildi! Yangilash:")
            book["author"] = input("Yangi muallif: ")
            book["year"] = input("Yangi yil: ")
            save_books(data)
            print(" Kitob malumoti yangilandi!")
            return
    print(" Kitob topilmadi.")

def delete_book():
    data = load_books()
    title = input("Qaysi kitobni ochirasiz (nomi): ")

    for book in data["books"]:
        if book["title"].lower() == title.lower():
            data["books"].remove(book)
            save_books(data)
            print("🗑 Kitob o‘chirildi!")
            return
    print("Kitob topilmadi.")


def main():
    while True:
        print(" Kitoblar Boshqaruv Dasturi ===")
        print("1. Yangi kitob qo‘shish")
        print("2. Kitobni yangilash")
        print("3. Kitobni o‘chirish")
        print("4. Barcha kitoblarni ko‘rish")
        print("5. Chiqish")

        choice = input("Tanlov: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            data = load_books()
            print(json.dumps(data, indent=4))
        elif choice == '5':
            print(" Dasturdan chiqildi.")
            break
        else:
            print(" Notogri tanlov, qayta urinib koring.")

if __name__ == "__main__":
    main()

import requests
import random

API_KEY = "YOUR_API_KEY"  
BASE_URL = "http://www.omdbapi.com/"

def get_movie_by_genre(genre):

    params = {
        "apikey": API_KEY,
        "s": genre,   
        "type": "movie"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("Response") == "False":
        print(" Hech qanday film topilmadi.")
        return

    movies = data.get("Search", [])
    movie = random.choice(movies)
 
    movie_id = movie["imdbID"]
    details = requests.get(BASE_URL, params={"apikey": API_KEY, "i": movie_id}).json()

    print(" Tavsiya etilgan film:")
    print("Sarlavha:", details.get("Title"))
    print("Yil:", details.get("Year"))
    print("Janr:", details.get("Genre"))
    print("Rejissor:", details.get("Director"))
    print("IMDB reyting:", details.get("imdbRating"))
    print("Tavsif:", details.get("Plot"))

if __name__ == "__main__":
    genre = input("Qaysi janrdagi filmni xohlaysiz? (masalan: action, comedy, drama): ")
    get_movie_by_genre(genre)
