# Используем стабильный Python 3.10
FROM python:3.10-slim

# Обновляем pip и устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Создаём рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Копируем requirements
COPY requirements_spleeter.txt /app/requirements.txt

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт, если нужен API
EXPOSE 5000

# Команда запуска (можно заменить на flask или python скрипт)
CMD ["python", "app.py"]
