FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY Kaggle.py .

RUN pip install -r requirements.txt

CMD ["python", "Kaggle.py"]
