from tests.logger_masks import logger


def get_mask_card_number(card_number: int) -> str:
    """Функция get_mask_card_number принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""

    try:
        card_str = str(card_number)
        logger.debug(f"Получен номер карты для обработки: {card_str}")

        if len(card_str) == 16:
            first_part = card_str[:6]
            masked_part = "** **** "
            last_part = card_str[12:]
            result = f"{first_part[:4]} {first_part[4:]}{masked_part}{last_part}"
            logger.info(f"Успешно создана маска карты: {result}")
            return result
        else:
            error_message = "номер карты не равен 16 символам"
            logger.error(f"Ошибка: {error_message}. Получено {len(card_str)} символов")
            return error_message

    except Exception:
        logger.exception("Произошла непредвиденная ошибка при обработке номера карты")
        return "Произошла ошибка при обработке номера карты"


def get_mask_account(account_number: int) -> str:
    """Функция get_mask_account принимает на вход номер счета в виде числа
    и возвращает его маску **XXXX"""

    try:
        account_str = str(account_number)
        logger.debug(f"Получен номер счета для обработки: {account_str}")

        if len(account_str) == 20:
            result = f"**{account_str[-4:]}"
            logger.info(f"Успешно создана маска счета: {result}")
            return result
        else:
            error_message = "номер счета не равен 20 символам"
            logger.error(f"Ошибка: {error_message}. Получено {len(account_str)} символов")
            return error_message

    except Exception:
        logger.exception("Произошла непредвиденная ошибка при обработке номера счета")
        return "Произошла ошибка при обработке номера счета"
