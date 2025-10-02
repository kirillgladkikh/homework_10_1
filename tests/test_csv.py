from unittest.mock import MagicMock

from src.get_csv_xls import read_transactions_from_csv

# Тестовые данные
test_csv_content = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"""


def test_read_transactions_success(monkeypatch):
    """
    Тест успешной работы функции чтения транзакций из CSV файла.
    """
    # Мокаем open
    mock_file = MagicMock()
    mock_file.return_value.__enter__.return_value.read.return_value = test_csv_content

    # Мокаем DictReader
    mock_dict_reader = MagicMock()
    mock_reader = MagicMock()
    mock_reader.__iter__.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    mock_dict_reader.return_value = mock_reader

    monkeypatch.setattr("builtins.open", mock_file)
    monkeypatch.setattr("csv.DictReader", mock_dict_reader)

    # Вызов тестируемой функции
    result = read_transactions_from_csv("dummy_path.csv")

    # Проверки
    assert len(result) == 2
    assert result[0]["id"] == "650703"
    assert result[1]["amount"] == "29740"
    mock_dict_reader.assert_called_once_with(mock_file.return_value.__enter__.return_value, delimiter=";")


def test_file_not_found(monkeypatch):
    """
    Тест обработки ситуации, когда файл не найден.
    """

    def mock_open(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr("builtins.open", mock_open)

    result = read_transactions_from_csv("non_existent_file.csv")
    assert result == []
