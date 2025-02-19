import os
import json
from datetime import datetime

# Файд для збереження історії пошуку
HISTORY_FILE = "history.json"

def load_history():
    """Завантажити історію з файлу."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Якщо файл пошкоджений або порожній, повертаємо порожній список
            return []
    return []

def save_history(history):
    """Зберегти історію у файл."""
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file)

def add_to_history(city, temperature):
    """Додати новий запис в історію."""
    history = load_history()

    # Оновити історію
    history.append({
        "city": city,
        "temperature": temperature,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    # Обмежити історію до 10 записів
    if len(history) > 10:
        history = history[-10:]

    save_history(history)

def get_history():
    """Отримати історію запитів."""
    return load_history()
