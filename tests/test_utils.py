import json
import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    def test_valid_file(self) -> None:
        """test_valid_file - проверяет корректную работу с валидным JSON-файлом"""
        # Создаем тестовые данные
        test_data = [{"id": 1, "amount": 100.0, "currency": "RUB"}, {"id": 2, "amount": 200.0, "currency": "USD"}]

        # Создаем mock для файла
        mock_file = mock_open(read_data=json.dumps(test_data))

        # Патчим функции os.path.exists и open
        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_file):
                result = load_transactions("test.json")

                # Проверяем результат
                self.assertEqual(result, test_data)

    def test_non_existent_file(self) -> None:
        """test_non_existent_file - проверяет обработку случая, когда файл не существует"""
        # Патчим os.path.exists чтобы файл "не существовал"
        with patch("os.path.exists", return_value=False):
            result = load_transactions("non_existent.json")
            self.assertEqual(result, [])

    def test_invalid_json(self) -> None:
        """test_invalid_json - проверяет обработку некорректного JSON"""
        # Создаем некорректный JSON
        mock_file = mock_open(read_data="{invalid_json}")

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_file):
                result = load_transactions("invalid.json")
                self.assertEqual(result, [])

    def test_not_list_data(self) -> None:
        """test_not_list_data - проверяет обработку случая, когда данные не являются списком"""
        # Создаем данные, которые не являются списком
        mock_file = mock_open(read_data=json.dumps({"key": "value"}))

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_file):
                result = load_transactions("not_list.json")
                self.assertEqual(result, [])

    def test_not_dict_items(self) -> None:
        """test_not_dict_items - проверяет обработку случая, когда элементы списка не являются словарями"""
        # Создаем список с не-dict элементами
        mock_file = mock_open(read_data=json.dumps([1, 2, 3]))

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_file):
                result = load_transactions("not_dict_items.json")
                self.assertEqual(result, [])

    def test_empty_file(self) -> None:
        """test_empty_file - проверяет обработку пустого файла"""
        # Создаем пустой файл
        mock_file = mock_open(read_data="")

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_file):
                result = load_transactions("empty.json")
                self.assertEqual(result, [])

    def test_general_exception(self) -> None:
        """test_general_exception - проверяет обработку общих исключений"""
        # Симулируем общую ошибку при чтении файла
        mock_file = MagicMock()
        mock_file.side_effect = Exception("Test exception")

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", mock_file):
                result = load_transactions("error.json")
                self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
