FROM python:3.10-slim

WORKDIR /spleeter

# Обновляем apt и устанавливаем ffmpeg + libsndfile (нужна Spleeter)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install --no-cache-dir \
    numpy==1.26.4 \
    tensorflow==2.9.3 \
    spleeter==2.4.0 \
    Flask==1.1.4 \
    Werkzeug==1.0.1 \
    click==7.1.2 \
    markupsafe==2.0.1

COPY app.py .

CMD ["python", "app.py"]

