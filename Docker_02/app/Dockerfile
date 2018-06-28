#la imagen base
FROM debian:jessie

#instale actualizaciones y python
RUN apt-get update && apt-get -y upgrade \
&& apt-get install -y python3 \
&& apt-get install -y python3-pip \
&& apt-get install -y build-essential libssl-dev libffi-dev python-dev \
&& apt-get update && apt-get -y upgrade python3-pip \
&& mkdir /opt/application

#EXPOSE
EXPOSE 5000

#copie mi aplicación
COPY . /opt/application

#estableci un directorio de trabajo
WORKDIR /opt/application

#instalando dependencias
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["app.py"]