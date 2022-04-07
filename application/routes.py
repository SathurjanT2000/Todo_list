from application import app
from flask import render_template
from application.forms import TaskForms
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_tasks', methods=["GET", "POST"])
def add_tasks():
    form = TaskForms()
    return render_template('add_tasks.html', form=form)
