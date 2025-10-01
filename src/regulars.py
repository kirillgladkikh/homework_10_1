import re
from typing import List, Dict
from collections import Counter


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Функция поиска банковских операций по описанию с использованием регулярных выражений.

    Параметры:
    data (List[Dict]): список словарей с данными о банковских операциях
    search (str): строка поиска, которую нужно найти в описании операций

    Возвращаемое значение:
    List[Dict]: список словарей с операциями, в описании которых найдено совпадение

    Пример использования:
    >>> transactions = [
    ...     {"id": 1, "description": "Перевод организации"},
    ...     {"id": 2, "description": "Оплата в магазине"},
    ...     {"id": 3, "description": "Перевод другу"}
    ... ]
    >>> process_bank_search(transactions, "перевод")
    [{'id': 1, 'description': 'Перевод организации'}]
    """
    # Создаем регулярное выражение с учетом регистра и пробелов
    pattern = re.compile(rf'\b{re.escape(search)}\b', re.IGNORECASE)

    # Фильтруем операции по описанию
    result = [
        transaction
        for transaction in data
        if 'description' in transaction and pattern.search(transaction['description'])
    ]

    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Функция подсчета количества операций по заданным категориям с использованием Counter.

    Параметры:
    data (List[Dict]): список словарей с данными о банковских операциях
    categories (List[str]): список категорий операций для подсчета

    Возвращаемое значение:
    Dict[str, int]: словарь, где ключи - категории, значения - количество операций

    Пример использования:
    >>> transactions = [
    ...     {"description": "Перевод организации"},
    ...     {"description": "Оплата в магазине"},
    ...     {"description": "Перевод организации"}
    ... ]
    >>> categories = ["Перевод организации", "Оплата в магазине"]
    >>> process_bank_operations(transactions, categories)
    {'Перевод организации': 2, 'Оплата в магазине': 1}
    """
    # Проверяем тип data
    if not isinstance(data, list):
        raise TypeError("Параметр data должен быть списком")

    # Проверяем, что все элементы data являются словарями
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы data должны быть словарями")

    # Проверяем тип categories
    if not isinstance(categories, list):
        raise TypeError("Параметр categories должен быть списком")

    # Добавляем проверку на пустой список категорий
    if not categories:
        raise ValueError("Список категорий не может быть пустым")

    # Собираем все описания операций в список
    descriptions = [transaction.get('description', '') for transaction in data]

    # Создаем Counter для подсчета всех описаний
    counter = Counter(descriptions)

    # Формируем итоговый результат только для указанных категорий
    result = {category: counter[category] for category in categories}

    return result
