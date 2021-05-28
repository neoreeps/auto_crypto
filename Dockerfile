FROM python:3.8-alpine

# Mountpoints for configuration & certificates
#VOLUME /conf
#VOLUME /certs

# Copy appdaemon into image
WORKDIR /opt/apps
COPY crontab start.sh crypto.env crypto.py exec_crypto.sh /opt/apps/

# Install timezone data
RUN apk add tzdata

# Install additional applications
RUN apk add bash
RUN apk add --update apk-cron && rm -rf /var/cache/apk/*
RUN /usr/bin/crontab crontab

# Install dependencies
RUN pip3 install cbpro

# Start script
ENTRYPOINT ["/opt/apps/start.sh"]
