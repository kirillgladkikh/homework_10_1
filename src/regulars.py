import re
from collections import Counter
from typing import Dict, List


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
    pattern = re.compile(rf"{re.escape(search)}", re.IGNORECASE)

    # Фильтруем операции по описанию
    result = [
        transaction
        for transaction in data
        if isinstance(transaction, dict)  # Проверяем, что элемент является словарем
        and "description" in transaction  # Проверяем наличие поля description
        and isinstance(transaction["description"], str)  # Проверяем тип description
        and pattern.search(transaction["description"])
    ]

    # Сортируем результат по id для предсказуемости
    result.sort(key=lambda x: x.get("id", 0))

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
    descriptions = [transaction.get("description", "") for transaction in data]

    # Создаем Counter для подсчета всех описаний
    counter = Counter(descriptions)

    # Формируем итоговый результат только для указанных категорий
    result = {category: counter[category] for category in categories}

    return result
