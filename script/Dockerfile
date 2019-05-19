FROM python:3.7

WORKDIR /home/script

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY mosquitto mosquitto

COPY withouthard.py checkpointId.txt ./

CMD ["python", "./withouthard.py"]
