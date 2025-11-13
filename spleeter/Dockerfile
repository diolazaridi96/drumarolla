# Базовый образ с Python 3.10
FROM python:3.10-slim

# Устанавливаем системные зависимости для Spleeter и аудио обработки
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /spleeter

# Копируем только requirements.txt сначала, чтобы кешировать слои
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код сплиттера
COPY . .

# Команда по умолчанию при запуске контейнера
# Здесь замените на ваш скрипт запуска Spleeter, например:
# python spleeter_service.py
CMD ["python", "spleeter_service.py"]
