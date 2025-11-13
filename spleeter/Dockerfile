FROM python:3.10-slim

WORKDIR /spleeter

RUN pip install --upgrade pip

# Совместимые версии
RUN pip install --no-cache-dir \
    tensorflow==2.9.3 \
    spleeter==2.4.0 \
    Flask==1.1.4 \
    Werkzeug==1.0.1 \
    click==7.1.2

COPY app.py .

CMD ["python", "app.py"]
