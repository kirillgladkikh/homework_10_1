import pytest

# from typing import List, Dict
# from collections import Counter
from src.regulars import process_bank_search

# Подготовим тестовые данные
TEST_TRANSACTIONS = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Оплата в магазине"},
    {"id": 3, "description": "Перевод другу"},
    {"id": 4, "description": "Снятие наличных"},
    {"id": 5, "description": "Оплата ЖКХ"},
    {"id": 6, "description": "перевод организации"},  # с маленьким регистром
]


def test_basic_search():
    """
    Тест базового поиска с точным совпадением
    """
    result = process_bank_search(TEST_TRANSACTIONS, "Перевод организации")
    expected = [{"id": 1, "description": "Перевод организации"}, {"id": 6, "description": "перевод организации"}]
    assert result == expected


def test_case_insensitive_search():
    """
    Тест поиска без учета регистра
    """
    result = process_bank_search(TEST_TRANSACTIONS, "перевод")
    expected = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 3, "description": "Перевод другу"},
        {"id": 6, "description": "перевод организации"},
    ]
    assert result == expected


def test_partial_match():
    """
    Тест частичного совпадения
    """
    result = process_bank_search(TEST_TRANSACTIONS, "организации")
    expected = [{"id": 1, "description": "Перевод организации"}, {"id": 6, "description": "перевод организации"}]
    assert result == expected


def test_no_matches():
    """
    Тест отсутствия совпадений
    """
    result = process_bank_search(TEST_TRANSACTIONS, "не существующая операция")
    assert result == []


def test_empty_search_string():
    """
    Тест с пустой строкой поиска
    """
    with pytest.raises(ValueError):
        process_bank_search(TEST_TRANSACTIONS, "")


def test_invalid_data_type():
    """
    Тест с некорректным типом данных
    """
    with pytest.raises(TypeError):
        process_bank_search("не список", "поиск")

    with pytest.raises(TypeError):
        process_bank_search(TEST_TRANSACTIONS, 123)  # не строка


def test_missing_description():
    transactions = [{"id": 1}, {"id": 2, "description": "Оплата в магазине"}, {"id": 3}]
    result = process_bank_search(transactions, "магазин")
    expected = [{"id": 2, "description": "Оплата в магазине"}]
    assert result == expected


def test_special_characters():
    transactions = [{"id": 1, "description": "Оплата (магазин)"}, {"id": 2, "description": "Оплата магазина!"}]
    result = process_bank_search(transactions, "(магазин)")
    expected = [{"id": 1, "description": "Оплата (магазин)"}]
    assert result == expected


def test_empty_transactions_list():
    """
    Тест с пустым списком транзакций
    """
    result = process_bank_search([], "любой поиск")
    assert result == []


def test_multiple_matches():
    transactions = [
        {"id": 1, "description": "Оплата магазина"},
        {"id": 2, "description": "Магазин электроники"},
        {"id": 3, "description": "Магазин одежды"},
    ]
    result = process_bank_search(transactions, "магазин")
    expected = [
        {"id": 1, "description": "Оплата магазина"},
        {"id": 2, "description": "Магазин электроники"},
        {"id": 3, "description": "Магазин одежды"},
    ]
    assert result == expected
