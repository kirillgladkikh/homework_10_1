import logging
import os
from datetime import datetime

# Формируем путь к директории логов
LOG_DIR = 'logs'

# Создаем директорию для логов, если её нет
if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
        print(f"Создана директория {LOG_DIR}")
    except OSError as e:
        print(f"Ошибка при создании директории логов: {e}")
        raise

# Формируем полное имя файла лога
log_file = os.path.join(LOG_DIR, f'masks_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
print(f"Путь к файлу лога: {log_file}")

# Настраиваем логгер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень логирования

# Создаем handler для записи в файл
try:
    file_handler = logging.FileHandler(log_file)
except Exception as e:
    print(f"Ошибка при создании FileHandler: {e}")
    raise

# Настраиваем формат логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Применяем форматер к handler
file_handler.setFormatter(file_formatter)

# Добавляем handler к логгеру
logger.addHandler(file_handler)

print("Logger initialized successfully")