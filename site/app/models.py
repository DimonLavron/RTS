from flask_login import UserMixin
from app import login


class User(UserMixin):
    id
    username = ''
    password = ''
    role = ''


@login.user_loader
def load_user(id):
    user = User()
    if id == 1:
        user.username = 'admin'
        user.password = 'admin'
        user.role = 'admin'
        user.id = 1

    if id == 2:
        user.username = 'organizer'
        user.password = 'organizer'
        user.role = 'organizer'
        user.id = 2
    return user

class Event:
    def __init__(self, checkpoint_id, tag, time):
        self.checkpoint_id = checkpoint_id
        self.tag = tag
        self.time = time

class Race:
    def __init__(self, name, admin, laps_number, lap_length, date_and_time_of_race, description):
        self.name = name
        self.admin = admin
        self.laps_number = laps_number
        self.lap_length = lap_length
        self.date_and_time_of_race = date_and_time_of_race
        self.description = description
