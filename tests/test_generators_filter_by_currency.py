import pytest

from data.data_generators import get_transactions
from src.generators import filter_by_currency

# Тест, проверяющий, что:
# функция корректно фильтрует транзакции по заданной валюте.
# функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.


# Фикстура для тестовых данных
@pytest.fixture
def sample_transactions() -> list:
    return get_transactions()


# Тест для filter_by_currency
@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        # Тестовые случаи для разных валют и количества транзакций в них
        ("USD", 2),  # Ожидаем 2 транзакции в USD
        ("RUB", 2),  # Ожидаем 2 транзакции в RUB
        ("EUR", 1),  # Ожидаем 1 транзакцию в EUR
        ("PND", 0),  # Ожидаем 0 транзакций в несуществующей валюте
    ],
)
def test_filter_by_currency_transactions_currency_quantity(
    sample_transactions: list, currency_code: str, expected_count: int
) -> None:
    """
    Тест проверяет поведение функции для разных валют и их вхождений во входном списке транзакций
    """
    # Получаем генератор отфильтрованных транзакций
    generator = filter_by_currency(sample_transactions, currency_code)

    # Собираем все результаты в список
    result = list(generator)

    # Проверяем количество результатов
    assert len(result) == expected_count

    # Дополнительно проверяем, что все транзакции имеют нужную валюту
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == currency_code


# Тест, проверяющий, что генератор не завершается ошибкой:
# при обработке пустого списка.
# или списка без соответствующих валютных операций.


# Фикстура для пустых данных
@pytest.fixture
def empty_transactions() -> list:
    return []


def test_filter_by_currency_empty_input(empty_transactions: list) -> None:
    """
    Тест проверяет поведение функции при пустом входном списке транзакций
    """
    # Проверяем работу с пустой валютой
    for currency_code in ["USD", "RUB", "EUR", "PND"]:
        # Получаем генератор отфильтрованных транзакций
        generator = filter_by_currency(empty_transactions, currency_code)

        # Собираем результаты в список
        result = list(generator)

        # Проверяем, что нет валют
        assert len(result) == 0

        # Проверяем, что результат пустой список
        assert result == []
