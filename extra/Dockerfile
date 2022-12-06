#Especifica la imagen base en este caso pythn a partir de la cual se creará la imagen vault
FROM python:3.8 

#Establecemos el directorio de trabajo en /proyecto
WORKDIR /proyecto 

#copiamos la aplicación cliente en el directorio de trabajo
COPY app.py /proyecto/ 

#descargar pip, vault y hvac
RUN python -m pip install --upgrade pip
RUN pip install vault
RUN pip install hvac

# Es necesario el puerto 8200tcp para poder conectarse con vault
EXPOSE 8200

#Ejecuta la aplicación app.py
CMD ["python3", "app.py"]

