from flask import Flask, render_template
import random

app = Flask(__name__)

smartphones_data = [
    {
        "name": "iPhone 15 Pro Max",
        "brand": "Apple",
        "year": 2023,
        "storage": "8/256, 8/512, 8/1TB",
        "os": "iOS 17",
        "screen": "LTPO 6.7''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#A61C00"],
        "price": "129 990 ₽"
    },
    {
        "name": "Samsung Galaxy S24 Ultra",
        "brand": "Samsung",
        "year": 2024,
        "storage": "12/256, 12/512, 12/1TB",
        "os": "One UI 6.1",
        "screen": "Dynamic AMOLED 6.8''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B4513", "#4A6FA5"],
        "price": "89 990 ₽"
    },
    {
        "name": "Google Pixel 8 Pro",
        "brand": "Google",
        "year": 2023,
        "storage": "12/128, 12/256, 12/512",
        "os": "Android 14",
        "screen": "LTPO 6.7''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B008B", "#4A6FA5"],
        "price": "79 990 ₽"
    },
    {
        "name": "Xiaomi 14 Pro",
        "brand": "Xiaomi",
        "year": 2024,
        "storage": "12/256, 16/512, 16/1TB",
        "os": "HyperOS",
        "screen": "LTPO 6.73''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#008000"],
        "price": "69 990 ₽"
    },
    {
        "name": "OnePlus 12",
        "brand": "OnePlus",
        "year": 2024,
        "storage": "12/256, 16/512, 16/1TB",
        "os": "OxygenOS 14",
        "screen": "LTPO 6.82''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B0000", "#4A6FA5"],
        "price": "59 990 ₽"
    },
    {
        "name": "Nothing Phone (2)",
        "brand": "Nothing",
        "year": 2023,
        "storage": "8/128, 12/256, 12/512",
        "os": "Nothing OS 2.5",
        "screen": "AMOLED 6.7''",
        "colors": ["#1F1F1F", "#E0E0E0"],
        "price": "49 990 ₽"
    },
    {
        "name": "Huawei P60 Pro",
        "brand": "Huawei",
        "year": 2023,
        "storage": "8/256, 8/512",
        "os": "HarmonyOS 4",
        "screen": "LTPO 6.67''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B008B", "#4A6FA5"],
        "price": "89 990 ₽"
    },
    {
        "name": "Realme GT 5 Pro",
        "brand": "Realme",
        "year": 2024,
        "storage": "12/256, 16/512, 16/1TB",
        "os": "Realme UI 5",
        "screen": "AMOLED 6.78''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B4513"],
        "price": "44 990 ₽"
    },
    {
        "name": "Vivo X100 Pro",
        "brand": "Vivo",
        "year": 2024,
        "storage": "12/256, 16/512",
        "os": "Funtouch OS 14",
        "screen": "AMOLED 6.78''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#008000"],
        "price": "74 990 ₽"
    },
    {
        "name": "Asus ROG Phone 8",
        "brand": "Asus",
        "year": 2024,
        "storage": "16/256, 16/512, 24/1TB",
        "os": "ROG UI",
        "screen": "AMOLED 6.78''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B0000"],
        "price": "84 990 ₽"
    },
    {
        "name": "Honor Magic 6 Pro",
        "brand": "Honor",
        "year": 2024,
        "storage": "12/256, 16/512",
        "os": "Magic OS 8",
        "screen": "LTPO 6.8''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#008000"],
        "price": "64 990 ₽"
    },
    {
        "name": "Sony Xperia 1 V",
        "brand": "Sony",
        "year": 2023,
        "storage": "12/256, 12/512",
        "os": "Android 13",
        "screen": "OLED 6.5''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5"],
        "price": "99 990 ₽"
    }
]

@app.route("/")
def home():
    random_phones = [random.choice(smartphones_data) for _ in range(75)]
    return render_template("index.html", phones=random_phones)

if __name__ == "__main__":
    app.run(debug=True)