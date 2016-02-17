FROM python:2.7.11

ADD requirements /tmp/requirements/

RUN pip install -r /tmp/requirements/requirements.txt

ADD . /app

WORKDIR /app

EXPOSE 80

CMD ["/usr/local/bin/python", "web.py"]
