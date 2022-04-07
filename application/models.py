from application import db
from datetime import datetime

class Tasks(db.Model):
    id = db.Columns(db.Integer, primary_key=True)
    description = db.Columns(db.String(100), nullable=False)
    completed = db.Columns(db.Boolean, nullable=False, default=False)
    date_created = db.Columns(db.Datetime, nullable=False, default=datetime.now())