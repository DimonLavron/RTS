from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import RegisterUserForm, RegisterCheckpointForm, LoginForm
from app.models import User, Event
from flask_login import current_user, login_user, logout_user

events_col = db.events


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if (current_user.is_authenticated):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'admin':
            user = User()
            user.username = 'admin'
            user.password = 'admin'
            user.role = 'admin'
            user.id = 1
            login_user(user)
            flash('{} is logged in. Welcome!'.format(user.username))
            return redirect(url_for('index'))
        elif form.username.data == 'organizer' and form.password.data == 'organizer':
            user = User()
            user.username = 'organizer'
            user.password = 'organizer'
            user.role = 'organizer'
            user.id = 2
            login_user(user)
            flash('{} is logged in. Welcome!'.format(user.username))
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route("/post", methods=['POST'])
def post():
	event1 = Event("10", "e280116060000206699a8abe4879", "2019-04-06 17:33:12")
	event2 = Event("20", "e280116060000206699a8abe4879", "2019-04-06 17:55:23")
	event3 = Event("30", "e280116060000206699a8abe4879", "2019-04-06 18:11:45")
	event4 = Event("40", "e280116060000206699a8abe4879", "2019-04-06 18:55:14")
	events_col.insert_many([
	{"checkpoint_id":event1.checkpoint_id, "tag":event1.tag, "time":event1.time},
	{"checkpoint_id":event2.checkpoint_id, "tag":event2.tag, "time":event2.time},
	{"checkpoint_id":event3.checkpoint_id, "tag":event3.tag, "time":event3.time},
	{"checkpoint_id":event4.checkpoint_id, "tag":event4.tag, "time":event4.time}
	])
	return redirect("/results")


@app.route("/results")
def table():
	heading = "Table with events"

	list = []
	for events in events_col.find() :
	   list.append(events)
	list.reverse()
	return render_template("table_bd.html",events = list, h=heading)



@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if (current_user.is_anonymous):
        return redirect(url_for('index'))
    form = RegisterUserForm()
    if form.validate_on_submit():
        flash('User {} {} is successfully registered.'.format(form.first_name.data, form.last_name.data))
        return redirect(url_for('index'))
    return render_template('register_user.html', form=form)


@app.route('/register_checkpoint', methods=['GET', 'POST'])
def register_checkpoint():
    if (current_user.is_anonymous):
        return redirect(url_for('index'))
    form = RegisterCheckpointForm()
    if form.validate_on_submit():
        flash('Checkpoint {} is successfully registered.'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('register_checkpoint.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
