import tkinter as tk
from tkinter import messagebox
from weather import get_weather
from history import get_history, add_to_history


# Функція для оновлення списку історії
def update_history_listbox():
    history = get_history()
    history_listbox.delete(0, tk.END)
    for record in history:
        history_listbox.insert(tk.END, f"{record['date']} - {record['city']}: {record['temperature']}°C")


# Функція для отримання погоди за введеним містом
def get_weather_data():
    city = city_entry.get()
    if city:
        try:
            weather_data = get_weather(city)
            temperature = weather_data["main"]["temp"]
            messagebox.showinfo("Погода", f"Температура в {city}: {temperature}°C")

            # Зберегти результат у історії
            add_to_history(city, temperature)
            update_history_listbox()
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося отримати дані: {e}")
    else:
        messagebox.showerror("Помилка", "Будь ласка, введіть місто!")


# Створення основного вікна
root = tk.Tk()
root.title("Прогноз погоди")
root.geometry("400x400")

# Введення міста
city_label = tk.Label(root, text="Введіть місто:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Кнопка для отримання погоди
get_weather_button = tk.Button(root, text="Отримати погоду", command=get_weather_data)
get_weather_button.pack(pady=10)

# Список історії запитів
history_label = tk.Label(root, text="Історія запитів:")
history_label.pack(pady=5)

history_listbox = tk.Listbox(root, width=40, height=10)
history_listbox.pack(pady=5)

# Оновити історію при запуску програми
update_history_listbox()

# Запуск програми
root.mainloop()
