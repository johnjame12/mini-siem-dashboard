from ..core.extensions import db
from datetime import datetime

class Threat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    source = db.Column(db.String(50))
    detail = db.Column(db.Text)
    action = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
