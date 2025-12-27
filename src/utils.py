import json
import os
from typing import Dict, List


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает данные о транзакциях из JSON-файла.
    Args:
        file_path (str): путь к JSON-файлу
    Returns:
        List[Dict]: список словарей с данными транзакций
    """
    # Проверяем существование файла
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что данные являются списком
            if not isinstance(data, list):
                print("Данные в файле не являются списком")
                return []

            # Проверяем, что все элементы списка являются словарями
            for item in data:
                if not isinstance(item, dict):
                    print("Элементы списка должны быть словарями")
                    return []

            return data

    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return []
