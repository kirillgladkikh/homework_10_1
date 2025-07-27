from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(input_str: str) -> str:
    """функция mask_account_card, которая умеет обрабатывать информацию как о картах, так и о счетах"""

    # Разделяем строку на части
    parts = input_str.split()

    # Получаем номер из последней части
    number = parts[-1]

    # Определяем тип и применяем соответствующую маску
    if 'Счет' in input_str:
        masked_number = get_mask_account(int(number))
    else:
        masked_number = get_mask_card_number(int(number))

    # Возвращаем результат
    return f"{' '.join(parts[:-1])} {masked_number}"
