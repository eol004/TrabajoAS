FROM python:3.8

#ENV VAULT_ADDR: "http://localhost:8200"

WORKDIR /proyecto

COPY app.py /proyecto/

#descargar vault
RUN python -m pip install --upgrade pip
RUN pip install vault
RUN pip install hvac

# Es necesario el puerto 8200tcp para poder conectarse con vault
EXPOSE 8200

CMD ["python3", "app.py"]
#ENTRYPOINT ["python3"]
