from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import RegisterUserForm, RegisterCheckpointForm
from flask_login import current_user
import csv

data = []


def get_info():
    global data
    with open("app/templates/runners.csv", encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]


def get_runner_by_id(id):
    for row in data:
        if row[1] == id:
            return row


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return "Login page"


@app.route('/results')
def table():
    get_info()
    table_data = [['Full Name', 'ID', 'Time']]
    collection = [['id003', '0:05:33'], ['id005', '0:06:02'], ['id001', '0:06:18'], ['id004', '0:06:49'], ['id002', '0:07:08']]
    for row in collection:
        temp = get_runner_by_id(row[0])
        temp.append(row[1])
        table_data.append(temp)
    return render_template('table.html', table=table_data)


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
