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

class Runner:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
