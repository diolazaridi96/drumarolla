FROM python:3.10-slim

WORKDIR /spleeter

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливаем совместимые версии
RUN pip install --no-cache-dir \
    tensorflow==2.9.3 \
    spleeter==2.4.0 \
    Flask==2.2.5 \
    Werkzeug==2.2.3

COPY app.py .

CMD ["python", "app.py"]
