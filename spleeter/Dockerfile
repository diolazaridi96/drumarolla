# Используем современный Python 3.10
FROM python:3.10-slim

# Рабочая папка в контейнере
WORKDIR /app

# Обновляем pip и setuptools
RUN pip install --upgrade pip setuptools wheel

# Устанавливаем последние стабильные версии Spleeter и TensorFlow
RUN pip install spleeter==2.4.2 tensorflow==2.12.1

# Открываем порт, если хочешь запускать API (например Flask)
EXPOSE 5000

# Можно запускать Spleeter через командную строку
ENTRYPOINT ["spleeter"]
