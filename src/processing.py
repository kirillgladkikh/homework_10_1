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
