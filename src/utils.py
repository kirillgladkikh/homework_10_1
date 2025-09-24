import json
import os

from tests.logger_utils import logger


def load_transactions(file_path: str):
    """
    Загружает данные о транзакциях из JSON-файла.
    Args:
        file_path (str): путь к JSON-файлу
    Returns:
        List[Dict]: список словарей с данными транзакций
    """
    try:
        # Проверяем существование файла
        if not os.path.exists(file_path):
            logger.error(f"Файл {file_path} не найден")
            return []

        logger.debug(f"Попытка загрузить файл: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                logger.debug("Данные успешно загружены из файла")

                # Проверяем, что данные являются списком
                if not isinstance(data, list):
                    logger.error("Данные в файле не являются списком")
                    return []

                # Проверяем, что все элементы списка являются словарями
                for item in data:
                    if not isinstance(item, dict):
                        logger.error("Элементы списка должны быть словарями")
                        return []

                logger.info("Данные успешно проверены и валидированы")
                return data

            except json.JSONDecodeError:
                logger.error("Ошибка декодирования JSON", exc_info=True)
                return []
            except Exception:
                logger.exception("Произошла непредвиденная ошибка при обработке файла")
                return []

    except Exception:
        logger.exception("Критическая ошибка при работе с файлом")
        return []
