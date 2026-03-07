# syntax=docker/dockerfile:1

# Imagen base de Python
FROM python:3.10-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src/ ./src/

# Exponer puerto
EXPOSE 8000

# Comando para producción (gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "src", "myproject.wsgi:application"]
