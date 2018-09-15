FROM python:2.7

RUN [ -d /opt ] || mkdir /opt && pip install Flask && pip install requests

COPY app.py /opt

RUN mkdir /opt/templates

ADD templates /opt/templates

EXPOSE 5000

CMD [ "python", "/opt/app.py" ]
