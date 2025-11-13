FROM python:3.10-slim

WORKDIR /spleeter

# Устанавливаем Spleeter и Flask
RUN pip install --no-cache-dir spleeter flask

COPY app.py .

CMD ["python", "app.py"]
