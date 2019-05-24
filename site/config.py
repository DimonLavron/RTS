import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    MQTT_BROKER_URL = 'mqtt'
    MQTT_BROKER_PORT = 1883
    MQTT_KEEPALIVE = 5
    UPLOADED_PHOTOS_DEST = os.getcwd()
