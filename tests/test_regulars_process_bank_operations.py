import pytest
from typing import List, Dict
from collections import Counter
from src.regulars import process_bank_operations

# Тестовые данные
TEST_TRANSACTIONS = [
    {
        "id": 1,
        "description": "Перевод организации"
    },
    {
        "id": 2,
        "description": "Оплата в магазине"
    },
    {
        "id": 3,
        "description": "Перевод организации"
    },
    {
        "id": 4,
        "description": "Снятие наличных"
    }
]


def test_basic_functionality():
    """
    Тест базовой функциональности: проверка подсчета операций
    """
    categories = ["Перевод организации", "Оплата в магазине"]
    expected = {"Перевод организации": 2, "Оплата в магазине": 1}
    result = process_bank_operations(TEST_TRANSACTIONS, categories)
    assert result == expected


def test_empty_data():
    """
    Тест на пустой список операций
    """
    categories = ["Перевод организации"]
    expected = {"Перевод организации": 0}
    result = process_bank_operations([], categories)
    assert result == expected


def test_missing_category():
    """
    Тест на категорию, которой нет в данных
    """
    categories = ["Оплата ЖКХ"]
    expected = {"Оплата ЖКХ": 0}
    result = process_bank_operations(TEST_TRANSACTIONS, categories)
    assert result == expected


def test_multiple_categories():
    """
    Тест на несколько категорий
    """
    categories = [
        "Перевод организации",
        "Оплата в магазине",
        "Снятие наличных"
    ]
    expected = {
        "Перевод организации": 2,
        "Оплата в магазине": 1,
        "Снятие наличных": 1
    }
    result = process_bank_operations(TEST_TRANSACTIONS, categories)
    assert result == expected


def test_no_description():
    """
    Тест на операции без поля description
    """
    transactions = [
        {"id": 1},
        {"id": 2, "description": "Перевод организации"},
        {"id": 3}
    ]
    categories = ["Перевод организации"]
    expected = {"Перевод организации": 1}
    result = process_bank_operations(transactions, categories)
    assert result == expected


def test_empty_categories():
    """
    Тест на пустой список категорий
    """
    with pytest.raises(ValueError):
        process_bank_operations(TEST_TRANSACTIONS, [])


def test_invalid_input():
    """
    Тест на некорректный ввод
    """
    with pytest.raises(TypeError):
        process_bank_operations("invalid", ["category"])

    with pytest.raises(TypeError):
        process_bank_operations(TEST_TRANSACTIONS, "invalid")
