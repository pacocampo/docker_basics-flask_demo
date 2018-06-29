#la imagen base
FROM alpine:3.6

#instale actualizaciones y python
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python3 \
&& pip3 install --upgrade pip \
&& mkdir -p /opt/application

#copie mi aplicación
COPY . /opt/application

#estableci un directorio de trabajo
WORKDIR /opt/application

#instalando dependencias
RUN pip3 install -r requirements.txt
