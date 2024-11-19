# Imagen base de Python
FROM python:3.9-slim-buster 

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos
COPY backend/requirements.txt requirements.txt

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Copiar los scripts SQL
COPY sql/ /app/sql/

# Comando para iniciar la aplicación FastAPI (ajusta según tu necesidad)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]