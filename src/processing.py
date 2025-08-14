from datetime import datetime

def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Параметры:
    data (list): список словарей для фильтрации
    state (str): значение состояния для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
    list: отфильтрованный список словарей
    """
    # Используем list comprehension для фильтрации
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, descending=True):
    """
    Сортирует список словарей по дате в порядке убывания или возрастания.

    Параметры:
    data (list): список словарей с записями
    descending (bool): True - сортировка по убыванию, False - по возрастанию

    Возвращает:
    list: отсортированный список словарей
    """
    # Сортируем список с использованием лямбда-функции и заданного порядка
    sorted_data = sorted(
        data,
        key=lambda item: datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=descending
    )
    return sorted_data
