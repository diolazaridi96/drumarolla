# Используем официальный Python 3.10
FROM python:3.10-slim

# Устанавливаем зависимости Spleeter
RUN pip install --no-cache-dir spleeter

# Создаём рабочую директорию
WORKDIR /spleeter

# Копируем скрипт для обработки
COPY app.py .

# Задаём команду по умолчанию
CMD ["python", "app.py"]
