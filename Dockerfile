# Используем стабильный Python 3.10 (совместим с Spleeter)
FROM python:3.10-slim

# Устанавливаем зависимости системы
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта
COPY . .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт для Flask
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
