from data.data_generators import get_transactions
from src.decorators import my_function

# from src.external_api import get_exchange_rate
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.get_csv_xls import read_transactions_from_csv, read_transactions_from_excel
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.regulars import process_bank_operations, process_bank_search
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

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
# print("\nДомашнее задание 12.1:")
# print("+Домашнее задание 12.2 (logger):")
# transactions = load_transactions("data/operations.json")
# print(transactions)
#
# for transaction in transactions:
#     # Проверяем наличие ключа operationAmount
#     if "operationAmount" in transaction:
#         # Получаем значение amount из словаря транзакций
#         transaction_amount = transaction["operationAmount"]["amount"]
#         transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
#         amount = get_exchange_rate(transaction_amount, transaction_currency_code)
#         print(f"Amount is: {amount} RUB (from {transaction_currency_code})")
#     else:
#         print("==============Предупреждение: операция без operationAmount")


# Домашнее задание 13.1
print("\nДомашнее задание 13.1:")

transactions = read_transactions_from_csv("data/transactions.csv")
print("\nGet from CSV:")
print(transactions)

transactions = read_transactions_from_excel("data/transactions_excel.xlsx")
print("\nGet from XLSX:")
print(transactions)


# Домашнее задание 13.2
print("\nДомашнее задание 13.2:")
transactions = read_transactions_from_csv("data/transactions.csv")

print("\nФункция №1: process_bank_search")
search_result = process_bank_search(transactions, "перевод")
print(search_result)

print("\nФункция №2: process_bank_operations")
# Определяем категории для подсчета
categories_list = ["Перевод организации", "Оплата в магазине"]

# Получаем результат
result = process_bank_operations(transactions, categories_list)
print(result)


def main():
    """
    Функция реализующая основную логику проекта
    """
    print("\nОСНОВНАЯ ЛОГИКА ПРОЕКТА:")
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        # Получаем ввод от пользователя
        user_input = input("Введите число от 1 до 3: ")

        try:
            # Преобразуем ввод в целое число
            number = int(user_input)

            # Проверяем, что число находится в допустимом диапазоне
            if number in (1, 2, 3):
                if number == 1:
                    print("Для обработки выбран JSON-файл.")
                    transactions = load_transactions("data/operations.json")
                elif number == 2:
                    print("Для обработки выбран CSV-файл.")
                    transactions = read_transactions_from_csv("data/transactions.csv")
                elif number == 3:
                    print("Для обработки выбран XLSX-файл.")
                    transactions = read_transactions_from_excel("data/transactions_excel.xlsx")
                break
            else:
                print("Ошибка: число должно быть 1, 2 или 3. Попробуйте еще раз.")
        except ValueError:
            print(f"Невозможно преобразовать '{user_input}' в целое число")

    # множество допустимых значений статусов фильтрации
    valid_statuses = {"executed", "canceled", "pending"}

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        # Получаем ввод от пользователя
        user_input = input()
        # Преобразуем ввод от пользователя в нижний регистр
        status = user_input.lower()

        if status in valid_statuses:
            result_list = filter_by_state(transactions, status.upper())
            # print(result_list)
            if status == "executed":
                print('Операции отфильтрованы по статусу "EXECUTED"')
            elif status == "canceled":
                print('Операции отфильтрованы по статусу "CANCELED"')
            elif status == "pending":
                print('Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    while True:
        # Получаем ввод от пользователя
        user_input = input("Отсортировать операции по дате? 1 - Да/ 2 - Нет: ")

        try:
            # Преобразуем ввод в целое число
            number = int(user_input)

            # Проверяем, что число находится в допустимом диапазоне
            if number in (1, 2):
                if number == 1:

                    while True:
                        # Получаем ввод от пользователя
                        user_input = input("Отсортировать по возрастанию (1) или по убыванию (2)? ")

                        try:
                            # Преобразуем ввод в целое число
                            order = int(user_input)

                            # Проверяем, что число находится в допустимом диапазоне
                            if order in (1, 2):
                                if order == 1:
                                    result_list = sort_by_date(result_list, False)
                                elif order == 2:
                                    result_list = sort_by_date(result_list, True)
                                # print(result_list)
                                break
                            else:
                                print("Ошибка: число должно быть 1 или 2. Попробуйте еще раз.")
                        except ValueError:
                            print(f"Невозможно преобразовать '{user_input}' в целое число")

                elif number == 2:
                    break
                break
            else:
                print("Ошибка: число должно быть 1 или 2. Попробуйте еще раз.")
        except ValueError:
            print(f"Невозможно преобразовать '{user_input}' в целое число")

    while True:
        # Получаем ввод от пользователя
        user_input = input("Выводить только рублевые транзакции? 1 - Да/ 2 - Нет: ")

        try:
            # Преобразуем ввод в целое число
            currency = int(user_input)

            # Проверяем, что число находится в допустимом диапазоне
            if currency in (1, 2):
                if currency == 1:
                    result_list = list(filter_by_currency(result_list, "RUB"))

                # for transaction in result_list:
                #     print(transaction)

                break
            else:
                print("Ошибка: число должно быть 1 или 2. Попробуйте еще раз.")
        except ValueError:
            print(f"Невозможно преобразовать '{user_input}' в целое число")

    while True:
        # Получаем ввод от пользователя
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? 1 - Да/ 2 - Нет: ")

        try:
            # Преобразуем ввод в целое число
            search = int(user_input)

            # Проверяем, что число находится в допустимом диапазоне
            if search in (1, 2):
                if search == 1:
                    result_list = process_bank_search(result_list, "перевод")

                # print(result_list)
                #
                # for transaction in result_list:
                #     print(transaction)

                break
            else:
                print("Ошибка: число должно быть 1 или 2. Попробуйте еще раз.")
        except ValueError:
            print(f"Невозможно преобразовать '{user_input}' в целое число")

    print("\nРаспечатываю итоговый список транзакций...")

    if len(result_list) != 0:
        print(f"Всего банковских операций в выборке: {len(result_list)}")

        for transaction in result_list:
            print(f"\n{transaction['date'][:10]} {transaction['description']}")
            print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
            print(
                f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}"
            )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    return


main()
