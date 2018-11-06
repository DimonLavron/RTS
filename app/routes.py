from app import app
from flask import render_template, redirect, url_for
from app.forms import RegisterUserForm, RegisterCheckpointForm
import csv

data = []


def get_info():
    global data
    with open("app/templates/runners.csv", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        data = [row for row in reader]


def get_runner_by_id(id):
    for row in data:
        if row[1] == id:
            return row


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    form = RegisterUserForm()
    if form.validate_on_submit():
        return redirect(url_for(index))
    return render_template('register_user.html', form=form)


@app.route('/register_checkpoint', methods=['GET', 'POST'])
def register_checkpoint():
    form = RegisterCheckpointForm()
    if form.validate_on_submit():
        return redirect(url_for(index))
    return render_template('register_checkpoint.html', form=form)


@app.route('/table')
def table():
    get_info()
    table_data = [['Full Name', 'ID', 'Time']]
    collection = [['id003', '0:05:33'], ['id005', '0:06:02'], ['id001', '0:06:18'], ['id004', '0:06:49'], ['id002', '0:07:08']]
    for row in collection:
        temp = get_runner_by_id(row[0])
        temp.append(row[1])
        table_data.append(temp)
    return render_template('table.html', table=table_data)
