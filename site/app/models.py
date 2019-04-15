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
