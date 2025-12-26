from flask import Flask, render_template, request, jsonify, session
import random
import os
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Важно для сессий!

# Файл для хранения пользователей
USERS_FILE = 'users.json'

# Загружаем пользователей из файла
def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

# Сохраняем пользователей в файл
def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# Добавляем начальных пользователей для теста
def init_users():
    users = load_users()
    if not users:  # Если файл пустой, добавляем тестового пользователя
        users.append({
            "username": "admin",
            "password": "123",
            "name": "Администратор"
        })
        save_users(users)

# Инициализируем пользователей при старте
init_users()
smartphones_data = [
    {
        "name": "iPhone 15 Pro Max",
        "brand": "Apple",
        "year": 2023,
        "storage": "8/256, 8/512, 8/1TB",
        "os": "iOS 17",
        "shell":"iOS 17",
        "screen": "LTPO 6.7''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#A61C00"],
        "price": "129 990 ₽"
    },
    {
        "name": "Samsung Galaxy S24 Ultra",
        "brand": "Samsung",
        "year": 2024,
        "storage": "12/256, 12/512, 12/1TB",
        "os": "Android",
        "shell": "One UI 6.1",
        "screen": "Dynamic AMOLED 6.8''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B4513", "#4A6FA5"],
        "price": "89 990 ₽"
    },
    {
        "name": "Google Pixel 8 Pro",
        "brand": "Google",
        "year": 2023,
        "storage": "12/128, 12/256, 12/512",
        "os": "Android",
        "shell": "PixelOS",
        "screen": "LTPO 6.7''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B008B", "#4A6FA5"],
        "price": "79 990 ₽"
    },
    {
        "name": "Xiaomi 14 Pro",
        "brand": "Xiaomi",
        "year": 2024,
        "storage": "12/256, 16/512, 16/1TB",
        "os": "Android",
        "shell": "HyperOS",
        "screen": "LTPO 6.73''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#008000"],
        "price": "69 990 ₽"
    },
    {
        "name": "OnePlus 12",
        "brand": "OnePlus",
        "year": 2024,
        "storage": "12/256, 16/512, 16/1TB",
        "os": "Android",
        "shell": "OxygenOS 14",
        "screen": "LTPO 6.82''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B0000", "#4A6FA5"],
        "price": "59 990 ₽"
    },
    {
        "name": "Nothing Phone (2)",
        "brand": "Nothing",
        "year": 2023,
        "storage": "8/128, 12/256, 12/512",
        "os": "Android",
        "shell": "Nothing OS 2.5",
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
        "shell": "HarmonyOS 4",
        "screen": "LTPO 6.67''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B008B", "#4A6FA5"],
        "price": "89 990 ₽"
    },
    {
        "name": "Realme GT 5 Pro",
        "brand": "Realme",
        "year": 2024,
        "storage": "12/256, 16/512, 16/1TB",
        "os": "Android",
        "shell": "Realme UI 5",
        "screen": "AMOLED 6.78''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B4513"],
        "price": "44 990 ₽"
    },
    {
        "name": "Vivo X100 Pro",
        "brand": "Vivo",
        "year": 2024,
        "storage": "12/256, 16/512",
        "os": "Android",
        "shell":"Funtouch OS 14",
        "screen": "AMOLED 6.78''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#008000"],
        "price": "74 990 ₽"
    },
    {
        "name": "Asus ROG Phone 8",
        "brand": "Asus",
        "year": 2024,
        "storage": "16/256, 16/512, 24/1TB",
        "os": "Android",
        "shell":"ROG UI",
        "screen": "AMOLED 6.78''",
        "colors": ["#1F1F1F", "#E0E0E0", "#8B0000"],
        "price": "84 990 ₽"
    },
    {
        "name": "Honor Magic 6 Pro",
        "brand": "Honor",
        "year": 2024,
        "storage": "12/256, 16/512",
        "os": "Android",
        "shell": "Magic OS 8",
        "screen": "LTPO 6.8''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5", "#008000"],
        "price": "64 990 ₽"
    },
    {
        "name": "Sony Xperia 1 V",
        "brand": "Sony",
        "year": 2023,
        "storage": "12/256, 12/512",
        "os": "Android",
        "screen": "OLED 6.5''",
        "colors": ["#1F1F1F", "#E0E0E0", "#4A6FA5"],
        "price": "99 990 ₽"
    }
]

@app.route("/")
def home():
    random_phones = [random.choice(smartphones_data) for _ in range(75)]
    return render_template("index.html", phones=random_phones)


@app.route("/load-users", methods=["GET"])
def load_users_route():
    users = load_users()
    # Возвращаем пользователей с паролями для проверки
    return jsonify(users)


@app.route("/save-user", methods=["POST"])
def save_user():
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")

    if not all([username, password, name]):
        return jsonify({"success": False, "message": "Все поля обязательны"}), 400

    users = load_users()

    # Проверяем, нет ли уже такого пользователя
    if any(u["username"] == username for u in users):
        return jsonify({"success": False, "message": "Пользователь уже существует"}), 400

    # Добавляем нового пользователя
    users.append({
        "username": username,
        "password": password,  # В реальном приложении пароли нужно хэшировать!
        "name": name
    })

    save_users(users)
    return jsonify({"success": True, "message": "Пользователь зарегистрирован"}), 200


@app.route("/check-login", methods=["POST"])
def check_login():
    username = request.form.get("username")
    password = request.form.get("password")

    users = load_users()
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)

    if user:
        session['user'] = user  # Сохраняем пользователя в сессии
        return jsonify({"success": True, "name": user["name"], "username": user["username"]})
    else:
        return jsonify({"success": False, "message": "Неверный логин или пароль"})


@app.route("/logout")
def logout():
    session.pop('user', None)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)