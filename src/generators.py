from typing import Generator, Tuple

def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор последовательности номеров карт"""

    # Проверяем корректность входных данных
    if not (1 <= start <= 9999999999999999):
        raise ValueError("Начальное значение должно быть от 1 до 9999999999999999")
    if not (1 <= end <= 9999999999999999):
        raise ValueError("Конечное значение должно быть от 1 до 9999999999999999")
    if start > end:
        raise ValueError("Начальное значение должно быть меньше или равно конечному")

    # Генерируем номера карт в заданном диапазоне
    for number in range(start, end + 1):
        # Форматируем число в строку с нулями и разделителями
        formatted_number = f"{number:016d}"
        card_number = f"{formatted_number[0:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"
        yield card_number
