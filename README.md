# Проект "Домашнее задание 10.1"

## Описание:

Проект "Домашнее задание 11.1" - это код на Python покрытый тестами (см. раздел "Тесты").

Содержит функции:

### модуль [masks.py](src%2Fmasks.py):

get_mask_card_number - принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX

get_mask_account - принимает на вход номер счета в виде числа и возвращает его маску **XXXX

### модуль [widget.py](src%2Fwidget.py):

mask_account_card - умеет обрабатывать информацию как о картах, так и о счетах.

get_date - принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")

### модуль [processing.py](src%2Fprocessing.py):

filter_by_state - фильтрует список словарей по значению ключа 'state'. Возвращает: отфильтрованный список словарей.

sort_by_date - сортирует список словарей по дате в порядке убывания или возрастания. Возвращает: отсортированный список словарей.

### модуль [generators.py](src%2Fgenerators.py)

filter_by_currency - принимает на вход список словарей, представляющих транзакции. Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.

transaction_descriptions - принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

card_number_generator - выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999. Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/kirillgladkikh/homework_10_1.git
```

2. Зависимости указаны в файле [pyproject.toml](pyproject.toml).

3. Для установки всех зависимостей из pyproject.toml используйте:
```
poetry install
```

## Использование:

1. Перейдите в файл [main.py](main.py).
2. Запустите файл [main.py](main.py).

## Примеры работы функций

### get_mask_card_number:

7000792289606361     # входной аргумент

7000 79** **** 6361  # выход функции

### get_mask_account:

73654108430135874305  # входной аргумент

**4305  # выход функции

### mask_account_card:

Visa Platinum 7000792289606361  # входной аргумент

Visa Platinum 7000 79** **** 6361  # выход функции

### get_date:

"2024-03-11T02:26:18.671407"  # входной аргумент

"ДД.ММ.ГГГГ" ("11.03.2024")  # выход функции

### filter_by_state:

Выход функции со статусом по умолчанию 'EXECUTED':

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Выход функции, если вторым аргументов передано 'CANCELED':

[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

### sort_by_date:

Выход функции (сортировка по убыванию, т. е. сначала самые последние операции):

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

### filter_by_currency

Выход функции для входных данных из [data_generators.py](data%2Fdata_generators.py), если вторым аргументов передано 'USD':

{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", to": "Счет 11776614605963066702"}
{"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}

### transaction_descriptions

Выход функции для входных данных из [data_generators.py](data%2Fdata_generators.py):

    Перевод организации 
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации

### card_number_generator

Выход функции (например для номеров карт от 1 до 5): 

    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005

## Тесты

Созданы тестовые модули:

для модуля [masks.py](src%2Fmasks.py): [test_masks.py](tests%2Ftest_masks.py) 

для модуля [widget.py](src%2Fwidget.py): [test_widget.py](tests%2Ftest_widget.py) 

для модуля [processing.py](src%2Fprocessing.py): [test_processing.py](tests%2Ftest_processing.py) 

для модуля [generators.py](src%2Fgenerators.py):
- [test_generators_filter_by_currency.py](tests%2Ftest_generators_filter_by_currency.py)
- [test_generators_transaction_descriptions.py](tests%2Ftest_generators_transaction_descriptions.py)
- [test_splitted_card_number_generator.py](tests%2Ftest_splitted_card_number_generator.py)

Также созданы:

- модуль [conftest.py](tests%2Fconftest.py) для исходных тестовых данных, содержащий фикстуры и параметризацию.
- модуль [data_generators.py](data%2Fdata_generators.py) - для исходных данных функций модуля [generators.py](src%2Fgenerators.py) и их тестов.


## Документация:

Настоящий файл [README.md](README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).