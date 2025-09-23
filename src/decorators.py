from functools import wraps
from typing import Any, Callable


def log(filename=None) -> Callable:
    """
    Декоратор для логирования выполнения функции.
    Если задан `filename`, лог записывается в файл, иначе выводится в консоль.
    """

    def decorator(func: Callable) -> Callable:
        """
        Возвращает обёртку, которая логирует выполнение функции `func`.
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обёртка для выполнения функции `func` с логированием её результата и ошибок.
            """
            try:
                result = func(*args, **kwargs)
                name_func = func.__name__

                # Формируем сообщение
                message = f"Функция {name_func} ок. Результат: {result}"

                # Записываем в файл или выводим в консоль
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result

            except ZeroDivisionError:
                error_message = f"{func.__name__} error: ZeroDivisionError. " f"Inputs: {args}, {kwargs}"
                return handle_error(error_message, filename)

            except Exception as e:
                error_message = f"{func.__name__} error: {str(e)}. " f"Inputs: {args}, {kwargs}"
                return handle_error(error_message, filename)

        return wrapper

    return decorator


def handle_error(message: str, filename: str) -> None:
    """
    Обрабатывает запись ошибки в файл или консоль.
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)
    raise  # Перебрасываем исключение после логирования


@log(filename="")
# @log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """
    Функция складывает два целых числа.
    """
    return x + y
