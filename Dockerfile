FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY untitled23.py .

RUN pip install -r requirements.txt

CMD ["python", "untitled23.py"]
