import pytest

from src.generators import card_number_generator

@pytest.mark.parametrize(
    "start, stop, expected_error",
    [
        # Проверка некорректного начального значения
        (0, 0, 'Начальное значение должно быть от 1 до 9999999999999999'),
        # Проверка некорректного конечного значения
        (9999999999999999, 10000000000000000, 'Конечное значение должно быть от 1 до 9999999999999999'),
        # Проверка некорректного диапазона
        (10, 1, 'Начальное значение должно быть меньше или равно конечному'),
    ],
)
def test_card_number_generator_invalid(start: int, stop: int, expected_error: str) -> None:
    with pytest.raises(ValueError) as expected_error_info:
        # Создаем генератор и сразу пытаемся получить первый элемент
        gen = card_number_generator(start, stop)
        next(gen)  # Это запустит выполнение генератора и проверки
    assert str(expected_error_info.value) == expected_error


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        # Проверка форматирования номеров карт
        (10, 10, ['0000 0000 0000 0010']),
        (1111, 1111, ['0000 0000 0000 1111']),
        (9999999999999999, 9999999999999999, ['9999 9999 9999 9999']),
        # Проверка корректного теста для диапазона номеров карт
        (10, 12, ['0000 0000 0000 0010', '0000 0000 0000 0011', '0000 0000 0000 0012']),
    ],
)
def test_card_number_generator_valid(start: int, stop: int, expected: list) -> None:
    generator = card_number_generator(start, stop)

    # Собираем все значения из генератора
    result = []
    while True:
        try:
            result.append(next(generator))
        except StopIteration:
            break

    # Проверяем, что все значения совпадают
    assert result == expected
