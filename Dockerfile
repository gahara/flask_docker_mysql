FROM python:3.7

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY microblog.py config.py docker-entrypoint.sh ./

RUN chmod +x docker-entrypoint.sh

ENV FLASK_APP microblog.py

EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]