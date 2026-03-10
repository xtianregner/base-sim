# syntax=docker/dockerfile:1

# Imagen base de Python
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Directorio de la aplicación
WORKDIR /app/src

# Recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# Exponer puerto
EXPOSE 8000

# Comando para producción (gunicorn)
CMD gunicorn myproject.wsgi --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120
