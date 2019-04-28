# BASE IMAGE
FROM python:3.7.2-alpine

# INSTALL DEPENDENCIES
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# SET WORKING DIRECTORY
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# ADD AND INSTALL REQUIREMENTS
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# ADD ENTRYPOINT.SH
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# ADD APP
COPY . /usr/src/app

# RUN SERVER
CMD ["/usr/src/app/entrypoint.sh"]
