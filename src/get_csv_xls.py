import pandas as pd
import csv
from typing import List, Dict


def read_transactions_from_csv(file_path: str = "data/transactions.csv") -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.
    Args: file_path (str): путь к CSV-файлу
    Returns: List[Dict]: список словарей с транзакциями
    """
    transactions = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            # Читаем CSV с разделителем ';'
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                # Преобразуем данные в нужный формат
                transaction = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "amount": row["amount"],
                    "currency_name": row["currency_name"],
                    "currency_code": row["currency_code"],
                    "from": row["from"],
                    "to": row["to"],
                    "description": row["description"],
                }

                transactions.append(transaction)

        return transactions

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        return []

    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")
        return []


def read_transactions_from_excel(file_path: str = 'data/transactions_excel.xlsx') -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.
    Args: file_path (str): путь к Excel-файлу
    Returns: List[Dict]: список словарей с транзакциями
    """
    try:
        # Читаем Excel файл
        df = pd.read_excel(file_path, engine='openpyxl', header=0)

        # Проверяем, что все необходимые столбцы присутствуют
        required_columns = [
            'id', 'state', 'date', 'amount',
            'currency_name', 'currency_code', 'from', 'to', 'description'
        ]

        if not all(column in df.columns for column in required_columns):
            raise ValueError("Файл Excel не содержит все необходимые столбцы")

        transactions = []

        for _, row in df.iterrows():
            try:
                # Преобразуем данные в нужный формат
                transaction = {
                    'id': row['id'],
                    'state': row['state'],
                    'date': row['date'],
                    'amount': row['amount'],
                    'currency_name': row['currency_name'],
                    'currency_code': row['currency_code'],
                    'from': row['from'],
                    'to': row['to'],
                    'description': row['description']
                }

                transactions.append(transaction)

            except Exception as e:
                print(f"Ошибка при обработке строки: {row}. Причина: {str(e)}")
                continue

        return transactions

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        return []

    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")
        return []
