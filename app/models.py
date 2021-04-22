from app import db
from dataclasses import dataclass


@dataclass
class Entry(db.Model):
    id: int
    body: str

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
