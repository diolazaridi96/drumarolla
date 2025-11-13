FROM python:3.10-slim

WORKDIR /spleeter

# Обновляем pip
RUN pip install --upgrade pip

# Совместимые версии всех зависимостей
RUN pip install --no-cache-dir \
    tensorflow==2.9.3 \
    spleeter==2.4.0 \
    Flask==2.1.3 \
    Werkzeug==2.1.2 \
    click==7.1.2

COPY app.py .

CMD ["python", "app.py"]
