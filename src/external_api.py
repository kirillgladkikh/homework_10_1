import requests

#API_KEY_EXCHANGE_RATES

url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount=1000.0"

headers = {
    "apikey": "q1xBP6wP6VEfymRmntgsFxdABB35xlKm"
}

# Выполняем GET-запрос к сайту и сохраняем ответ в переменную response
response = requests.get(url, headers=headers)

# Получаем статус-код из ответа и выводим его на экран
status_code = response.status_code
print(f"Статус код: {status_code}")

# Проверяем, равен ли статус-код 200, то есть чтобы запрос был успешным
if status_code == 200:
    # Выводим содержимое сайта на экран
    content = response.text
    print(f"Содержимое сайта:\n{content}")
else:
    # Выводим сообщение об ошибке
    print(f"Запрос не был успешным. Возможная причина: {response.reason}")