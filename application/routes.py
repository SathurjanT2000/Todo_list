from application import app, db
from flask import render_template, request
from application.forms import TaskForms
from application.models import Tasks

@app.route('/')
def index():
    all_tasks = Tasks.query.all()
    return render_template('index.html', all_tasks=all_tasks)

@app.route('/add_tasks', methods=["GET", "POST"])
def add_tasks():
    form = TaskForms()

    if request.method == "POST":
        task = Tasks(description=form.description.data)
        db.session.add(task)
        db.session.commit()

    return render_template('add_tasks.html', form=form)
