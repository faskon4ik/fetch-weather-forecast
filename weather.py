import requests

API_KEY = "de0902d81402af1e033009df5cd09ac2"  # ключ API OpenWeatherMap


def get_weather(city):
    """Отримати дані про погоду для заданого міста."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"Помилка: {data['message']}")

    return data
