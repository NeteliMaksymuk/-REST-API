FROM python:3.10.6-slim

ENV FLASK_APP=project

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY project /opt/project

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
