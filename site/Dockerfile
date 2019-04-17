FROM python:3.7-alpine

RUN adduser -D rts

WORKDIR /home/site

COPY requirements.txt requirements.txt
RUN python -m venv venv-site
RUN venv-site/bin/pip install -r requirements.txt
RUN venv-site/bin/pip install gunicorn

COPY app app
COPY rts.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP rts.py

RUN chown -R rts:rts ./
USER rts

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
