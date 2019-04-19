import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    MQTT_BROKER_URL = 'mqtt'
    MQTT_BROKER_PORT = 1883
    # MQTT_USERNAME = ''
    # MQTT_PASSWORD = ''
    MQTT_KEEPALIVE = 5
