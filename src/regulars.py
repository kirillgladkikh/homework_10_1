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


# Пример использования с предоставленными данными
if __name__ == "__main__":
    test_transactions = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]


