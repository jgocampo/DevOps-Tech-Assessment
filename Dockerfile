# Imagen base
FROM public.ecr.aws/g7r9o2q3/python-3.9-slim-buster:latest

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
