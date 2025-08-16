def get_mask_card_number(card_number: int) -> str:
    """Функция get_mask_card_number принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""

    # Преобразуем номер карты в строку
    card_str = str(card_number)

    # Разделяем первые 6 цифр
    first_part = card_str[:6]

    # Формируем среднюю часть с масками
    masked_part = "** **** "

    # Получаем последние 4 цифры
    last_part = card_str[12:]

    # Формируем итоговую маску с пробелами
    return f"{first_part[:4]} {first_part[4:]}{masked_part}{last_part}"


def get_mask_account(account_number: int) -> str:
    """Функция get_mask_account принимает на вход номер счета в виде числа
    и возвращает его маску **XXXX"""

    # Преобразуем номер счета в строку
    account_str = str(account_number)

    # Формируем итоговую маску
    return f"**{account_str[-4:]}"
