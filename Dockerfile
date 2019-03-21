FROM python:3.6-alpine

RUN adduser -D rts

WORKDIR /home/rts-site

COPY requirements.txt requirements.txt
RUN python -m venv venv-rts
RUN venv-rts/bin/pip install -r requirements.txt
RUN venv-rts/bin/pip install gunicorn

COPY app app
COPY rts.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP rts.py

RUN chown -R rts:rts ./
USER rts

EXPOSE 5000
ENTRYPOINT ["sh", "./boot.sh"]