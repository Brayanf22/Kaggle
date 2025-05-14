FROM python:3.11-slim

# ❶ Directorio de trabajo
WORKDIR /app

# ❷ Copiar dependencias
COPY requirements.txt .

# ❸ Copiar tu script
COPY kaggle.py .

# ❹ Instalar
RUN pip install --no-cache-dir -r requirements.txt

# ❺ Comando por defecto
CMD ["python", "kaggle.py"]

