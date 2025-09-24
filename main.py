from data.data_generators import get_transactions
from src.decorators import my_function
from src.external_api import get_exchange_rate
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card
from src.get_csv_xls import read_transactions_from_csv, read_transactions_from_excel

# Домашнее задание 9.1
print("\nДомашнее задание 9.1:")
print("+Домашнее задание 12.2 (logger):")
print(get_mask_card_number(1234567890123456))
print(get_mask_account(73654108430135874305))

# Домашнее задание 9.2
print("\nДомашнее задание 9.2:")
print(mask_account_card("Maestro 1596837868705199"))
print(get_date("2024-03-11T02:26:18.671407"))

# Домашнее задание 10.1
print("\nДомашнее задание 10.1:")

list_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(list_data, "EXECUTED"))
print(sort_by_date(list_data, True))

# Домашнее задание 11.1
print("\nДомашнее задание 11.1:")

# Подставляем исходные данные из модуля data_generators.py
data = get_transactions()

# Выполняем функцию filter_by_currency

# Получаем данные из функции filter_by_currency
# без генерации ошибки выполнения
# для любого количества результатов генератора
# и для любой валюты
currency_transactions = filter_by_currency(data, "USD")
for transaction in currency_transactions:
    print(transaction)

# Выполняем функцию transaction_descriptions
descriptions = transaction_descriptions(data)
for description in descriptions:
    print(description)


# Выполняем функцию card_number_generator
try:
    for card_number in card_number_generator(10, 1):
        print(card_number)
except ValueError as e:
    print(f"Произошла ошибка: {e}")


# Домашнее задание 11.2
print("\nДомашнее задание 11.2:")

my_function(4, 2)


# Домашнее задание 12.1
print("\nДомашнее задание 12.1:")
print("+Домашнее задание 12.2 (logger):")
# transactions = load_transactions("data/operations.json")
# print(transactions)

# for transaction in transactions:
# Проверяем наличие ключа operationAmount
#    if "operationAmount" in transaction:
#        # Получаем значение amount из словаря транзакций
#        transaction_amount = transaction["operationAmount"]["amount"]
#        transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
#        amount = get_exchange_rate(transaction_amount, transaction_currency_code)
#        print(f"Amount is: {amount} RUB (from {transaction_currency_code})")
#    else:
#        print("==============Предупреждение: операция без operationAmount")

# Домашнее задание 13.1
print("\nДомашнее задание 13.1:")

transactions = read_transactions_from_csv("data/transactions.csv")
print('\nGet from CSV:')
print(transactions)

transactions = read_transactions_from_excel('data/transactions_excel.xlsx')
print('\nGet from XLSX:')
print(transactions)
