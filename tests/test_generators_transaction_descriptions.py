import pytest

from data.data_generators import get_transactions
from src.generators import transaction_descriptions

# Тест, проверяющий, что функция возвращает корректные описания для каждой транзакции.


# Фикстура для тестовых данных
@pytest.fixture
def sample_transactions() -> list:
    return get_transactions()


# Фикстура для ожидаемых описаний
@pytest.fixture
def expected_descriptions() -> list:
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions(sample_transactions: list, expected_descriptions: list) -> None:
    """
    Тест проверяет корректность извлечения описаний транзакций
    """
    # Получаем генератор описаний
    descriptions = transaction_descriptions(sample_transactions)

    # Преобразуем генератор в список
    result = list(descriptions)

    # Проверяем количество полученных описаний
    assert len(result) == len(expected_descriptions)

    # Проверяем каждое описание через прямой доступ к индексам
    for i in range(len(result)):
        actual = result[i]
        expected = expected_descriptions[i]
        assert actual == expected


# Тест, который тестирует работу функции с различным количеством входных транзакций
# Фикстура для получения входных данных
@pytest.fixture
def base_transactions() -> list:
    return get_transactions()


# Тест с различными количествами транзакций
@pytest.mark.parametrize(
    "num_transactions, expected_length",
    [
        (0, 0),  # Пустой список
        (1, 1),  # Одна транзакция
        (2, 2),  # Две транзакции
        (3, 3),  # Три транзакции
        (5, 5),  # Все транзакции
    ],
)
def test_transaction_descriptions_count(base_transactions: list, num_transactions: int, expected_length: int) -> None:
    """
    Тест проверяет работу функции с различным количеством транзакций
    """
    # Берем срез транзакций нужной длины
    test_transactions = base_transactions[:num_transactions]

    # Получаем генератор описаний
    descriptions = transaction_descriptions(test_transactions)

    # Преобразуем в список
    result = list(descriptions)

    # Проверяем длину результата
    assert len(result) == expected_length


# Тест, проверяющий, что генератор не завершается ошибкой:
# при обработке пустого списка.


# Фикстура для пустых данных
@pytest.fixture
def empty_transactions() -> list:
    return []


def test_transaction_descriptions_empty_input(empty_transactions: list) -> None:
    """
    Тест проверяет поведение функции при пустом входном списке транзакций
    """
    # Получаем генератор отфильтрованных транзакций
    generator = transaction_descriptions(empty_transactions)

    # Собираем результаты в список
    result = list(generator)

    # Проверяем, что результат пустой список
    assert result == []
