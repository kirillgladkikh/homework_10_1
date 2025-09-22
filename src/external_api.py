import requests

#API_KEY_EXCHANGE_RATES

def get_exchange_rate(transaction_amount: str ='1000.0', currency: str ='RUB') -> float:
    """
    Функция для получения обменного курса и конвертации суммы
    :param transaction_amount: сумма для конвертации (по умолчанию 1000.0)
    :param currency: валюта (по умолчанию 'RUB')
    :return: конвертированная сумма в рублях
    """
    if currency != 'RUB':
        # url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount=1000.0"
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={transaction_amount}'
        headers = {"apikey": "q1xBP6wP6VEfymRmntgsFxdABB35xlKm"}

        # Выполняем GET-запрос к сайту и сохраняем ответ в переменную response
        response = requests.get(url, headers=headers)

        data = response.json()  # Преобразуем ответ в словарь

        # Извлекаем из API-запроса сумму транзакции в рублях
        amount = data['result']

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
    else:
        amount = transaction_amount
    return float(amount)