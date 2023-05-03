# Imagen base
FROM python:3.9-slim-buster

# Establece el directorio de trabajo en la imagen
WORKDIR /app

# Copia los archivos necesarios a la imagen
COPY requirements.txt .
COPY app.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 80 en la imagen
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
