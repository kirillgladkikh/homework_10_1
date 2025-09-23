import logging
import os
from datetime import datetime
import sys

# Получаем путь к корню проекта
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Формируем путь к директории логов
LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')

# Создаем директорию для логов, если её нет
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Формируем полное имя файла лога
log_file = os.path.join(LOG_DIR, f'masks_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')

# Настраиваем логгер для модуля masks
logger = logging.getLogger('masks')
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