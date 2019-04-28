# BASE IMAGE
FROM python:3.7.2-alpine

# SET WORKING DIRECTORY
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# ADD AND INSTALL REQUIREMENTS
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# ADD APP
COPY . /usr/src/app

# RUN SERVER
CMD python manage.py run -h 0.0.0.0
