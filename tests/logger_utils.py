import logging
import os
import json
from datetime import datetime
from typing import Dict, List

# Получаем путь к корню проекта
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Создаем директорию для логов, если её нет
LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Формируем имя файла лога
log_file = os.path.join(LOG_DIR, f'utils_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')

# Создаем логгер
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень логирования

# Создаем handler для записи в файл
file_handler = logging.FileHandler(log_file)

# Настраиваем формат логов
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Применяем форматер к handler
file_handler.setFormatter(file_formatter)

# Добавляем handler к логгеру
logger.addHandler(file_handler)