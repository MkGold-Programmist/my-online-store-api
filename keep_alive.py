import time
import urllib.request

# Укажите ссылку на ваш эндпоинт здоровья (или корень сайта)
URL = "https://my-online-store-api.onrender.com/"

# Интервал в секундах (например, каждые 10 минут = 600 секунд)
INTERVAL = 600

print("Пинг-сервер запущен. Для остановки нажмите Ctrl+C.")

while True:
  try:
    # Отправляем GET-запрос
    with urllib.request.urlopen(URL) as response:
      print(f"[{time.strftime('%X')}] Пинг успешен! Статус: {response.status}")
  except Exception as e:
    print(f"[{time.strftime('%X')}] Ошибка при пинге: {e}")

  # Ждем перед следующим запросом
  time.sleep(INTERVAL)