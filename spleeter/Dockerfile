FROM python:3.10-slim

WORKDIR /spleeter

# Обновляем pip и устанавливаем совместимые зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir \
    tensorflow==2.10.0 \
    spleeter==2.4.0 \
    Flask==2.2.5 \
    Werkzeug==2.2.3

COPY app.py .

CMD ["python", "app.py"]
