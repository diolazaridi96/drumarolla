FROM python:3.10-slim

WORKDIR /spleeter

# Устанавливаем совместимые версии Flask и Werkzeug
RUN pip install --no-cache-dir spleeter Flask==2.2.5 Werkzeug==2.2.3

COPY app.py .

CMD ["python", "app.py"]
