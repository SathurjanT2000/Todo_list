from application import app, db
from flask import render_template, request, redirect, url_for
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
        return redirect(url_for('index'))

    return render_template('add_tasks.html', form=form)

@app.route('/complete/<int:completed>/<int:id>')
def complete_task(completed, id):
    task = Tasks.query.get(id)
    task.completed = bool(completed)
    db.session.commit()
    return redirect(url_for('index'))
