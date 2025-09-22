import unittest
from unittest.mock import patch, MagicMock
from src.external_api import get_exchange_rate


class TestExchangeRate(unittest.TestCase):

    @patch("src.external_api.API_KEY", "q1xBP6wP6VEfymRmntgsFxdABB35xlKm")  # Патч API_KEY напрямую
    @patch("requests.get")  # Патч requests.get
    def test_successful_conversion(self, mock_get):
        # Проверяем, что API_KEY установлен правильно
        from src.external_api import API_KEY

        self.assertEqual(API_KEY, "q1xBP6wP6VEfymRmntgsFxdABB35xlKm")

        # Создаем mock-ответ сервера
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 1234.56, "status": "success"}

        # Настраиваем mock для метода get
        mock_get.return_value = mock_response

        # Вызываем тестируемую функцию
        result = get_exchange_rate(transaction_amount="1000.0", currency="USD")

        # Проверяем результат
        self.assertEqual(result, 1234.56)

        # Проверяем, что запрос был сделан с правильными параметрами
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1000.0",
            headers={"apikey": "q1xBP6wP6VEfymRmntgsFxdABB35xlKm"},
        )

    @patch("requests.get")
    def test_same_currency(self, mock_get):
        # Проверяем случай, когда валюта совпадает с RUB
        result = get_exchange_rate(transaction_amount="1000.0", currency="RUB")
        self.assertEqual(result, 1000.0)

        # Убеждаемся, что запрос не был сделан
        mock_get.assert_not_called()

    # @patch('requests.get')
    # def test_failed_conversion(self, mock_get):
    # Симулируем ошибку сервера
    # mock_response = MagicMock()
    # mock_response.status_code = 500
    # mock_response.json.return_value = {
    # "error": "Internal Server Error"
    # }
    # mock_get.return_value = mock_response

    # Проверяем обработку ошибки
    # result = get_exchange_rate(transaction_amount="1000.0", currency="USD")
    # self.assertEqual(result, 0.0)  # или другое значение по умолчанию


if __name__ == "__main__":
    unittest.main()
