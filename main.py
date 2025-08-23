from data.data_generators import get_transactions
from src.generators import filter_by_currency, card_number_generator
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Домашнее задание 9.1
print('\nДомашнее задание 9.1:')
print(get_mask_card_number(1234567890123456))
print(get_mask_account(73654108430135874305))

# Домашнее задание 9.2
print('\nДомашнее задание 9.2:')
print(mask_account_card("Maestro 1596837868705199"))
print(get_date("2024-03-11T02:26:18.671407"))

# Домашнее задание 10.1
print('\nДомашнее задание 10.1:')

list_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(list_data, "EXECUTED"))
print(sort_by_date(list_data, True))

# Домашнее задание 11.1
print('\nДомашнее задание 11.1:')

# Выполняем функцию filter_by_currency

# Подставляем исходные данные из модуля data_generators.py
data = get_transactions()

# Получаем данные из функции filter_by_currency
# без генерации ошибки выполнения
# для любого количества результатов генератора
# и для любой валюты
currency_transactions = filter_by_currency(data, "PND")
for transaction in currency_transactions:
    print(transaction)


# Выполняем функцию card_number_generator
try:
    for card_number in card_number_generator(10, 1):
        print(card_number)
except ValueError as e:
    print(f"Произошла ошибка: {e}")
