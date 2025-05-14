FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY kaggle.py.

RUN pip install -r requirements.txt

CMD ["python", "kaggle.py"]
