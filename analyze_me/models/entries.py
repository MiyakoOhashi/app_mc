#analyze_me/models/entries.py       2020/9/29   M.O
from analyze_me import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime)

    def __init__(self, email=None, name=None, password=None):
        self.email = email
        self.name = name
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} name:{} email:{}>'.format(self.id, self.name, self.email)