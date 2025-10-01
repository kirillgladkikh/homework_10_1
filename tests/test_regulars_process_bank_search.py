import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Функция поиска банковских операций по описанию с использованием регулярных выражений.

    Параметры:
    data (List[Dict]): список словарей с данными о банковских операциях
    search (str): строка поиска, которую нужно найти в описании операций

    Возвращаемое значение:
    List[Dict]: список словарей с операциями, в описании которых найдено совпадение
    """
    # Проверяем корректность входных данных
    if not isinstance(data, list):
        raise TypeError("Параметр data должен быть списком")

    if not isinstance(search, str):
        raise TypeError("Параметр search должен быть строкой")

    if not search.strip():
        raise ValueError("Строка поиска не может быть пустой")

    # Создаем регулярное выражение с учетом регистра и пробелов
    pattern = re.compile(rf'\b{re.escape(search)}\b', re.IGNORECASE)

    # Фильтруем операции по описанию
    result = [
        transaction
        for transaction in data
        if isinstance(transaction, dict) and  # Проверяем, что элемент является словарем
           'description' in transaction and  # Проверяем наличие поля description
           isinstance(transaction['description'], str) and  # Проверяем тип description
           pattern.search(transaction['description'])
    ]

    # Сортируем результат по id для предсказуемости
    result.sort(key=lambda x: x.get('id', 0))

    return result