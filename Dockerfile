FROM python:3.9-alpine
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN mkdir /app
WORKDIR /app
ENV FLASK_APP=app.py
COPY requirements.txt /app/requirements.txt
RUN pip install databases
RUN pip install SQLAlchemy
RUN pip install requests-cache
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app
CMD ["flask", "run"]