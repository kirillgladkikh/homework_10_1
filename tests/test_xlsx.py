from unittest.mock import patch

import pytest
from pandas import DataFrame

from src.get_csv_xls import read_transactions_from_excel

# Пример тестовых данных
TEST_DATA = {
    "id": [1, 2],
    "state": ["EXECUTED", "EXECUTED"],
    "date": ["2023-09-05", "2023-09-06"],
    "amount": [1000, 2000],
    "currency_name": ["RUB", "USD"],
    "currency_code": ["RUB", "USD"],
    "from": ["Счет 123", "Карта 456"],
    "to": ["Счет 789", "Карта 012"],
    "description": ["Перевод", "Оплата"],
}


@patch("pandas.read_excel")
def test_read_transactions_success(mock_read_excel):
    """
    Тест успешной работы функции чтения транзакций из Excel файла.
    """
    # Создаем моковый DataFrame
    mock_df = DataFrame(TEST_DATA)
    mock_read_excel.return_value = mock_df

    # Вызываем тестируемую функцию
    result = read_transactions_from_excel("test_file.xlsx")

    # Проверки
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["amount"] == 2000
    mock_read_excel.assert_called_once_with("test_file.xlsx", engine="openpyxl", header=0)


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_file_not_found(mock_read_excel):
    """
    Тест обработки ситуации, когда Excel файл не найден.
    """
    result = read_transactions_from_excel("non_existent_file.xlsx")
    assert result == []
    mock_read_excel.assert_called_once_with("non_existent_file.xlsx", engine="openpyxl", header=0)


@patch("pandas.read_excel", side_effect=Exception)
def test_general_exception(mock_read_excel):
    """
    Тест обработки общих исключений при чтении Excel файла.
    """
    result = read_transactions_from_excel("error_file.xlsx")
    assert result == []
    mock_read_excel.assert_called_once_with("error_file.xlsx", engine="openpyxl", header=0)


if __name__ == "__main__":
    pytest.main()
