FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY kaggle.py .        # <— aquí el punto como destino

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "kaggle.py"]

