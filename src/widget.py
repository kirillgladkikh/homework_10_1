from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str) -> str:
    """функция mask_account_card, которая умеет обрабатывать информацию как о картах, так и о счетах"""

    # Разделяем строку на части
    parts = input_str.split()

    # Получаем номер из последней части
    number = parts[-1]

    # Определяем тип и применяем соответствующую маску
    if "Счет" in input_str:
        masked_number = get_mask_account(int(number))
    else:
        masked_number = get_mask_card_number(int(number))

    # Возвращаем результат
    return f"{' '.join(parts[:-1])} {masked_number}"


def get_date(input_str: str) -> str:
    """функция принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" ("11.03.2024")"""

    part_3: str = input_str[:4]
    part_2: str = input_str[5:7]
    part_1: str = input_str[8:10]

    return f"{part_1}.{part_2}.{part_3}"
