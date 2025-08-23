import pytest
from src.generators import filter_by_currency
from data.data_generators import get_transactions


# Фикстура для тестовых данных
@pytest.fixture
def sample_transactions():
    return get_transactions()


# Тест для filter_by_currency
@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        # Тестовые случаи для разных валют и количества транзакций в них
        ("USD", 2),  # Ожидаем 2 транзакции в USD
        ("RUB", 2),  # Ожидаем 2 транзакции в RUB
        ("EUR", 1),  # Ожидаем 1 транзакцию в EUR
        ("PND", 0)  # Ожидаем 0 транзакций в несуществующей валюте
    ]
)
def test_filter_by_currency(sample_transactions: list, currency_code: str, expected_count: int) -> None:
    # Получаем генератор отфильтрованных транзакций
    generator = filter_by_currency(sample_transactions, currency_code)

    # Собираем все результаты в список
    result = list(generator)

    # Проверяем количество результатов
    assert len(result) == expected_count

    # Дополнительно проверяем, что все транзакции имеют нужную валюту
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == currency_code

