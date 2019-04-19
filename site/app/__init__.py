from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_mqtt import Mqtt
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)

client = MongoClient("db:27017")
db = client.mymongodb

mqtt = Mqtt(app)

from app import routes
