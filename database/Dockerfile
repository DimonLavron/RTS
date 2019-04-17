FROM python:3.6-alpine

RUN adduser -D app

WORKDIR /home/database

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY templates templates
COPY static static

COPY app.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app.py

RUN chown -R app:app ./
USER app

EXPOSE 8000
ENTRYPOINT ["./boot.sh"]
