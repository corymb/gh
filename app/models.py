from datetime import datetime

from app import db


class Confession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    confession = db.Column(db.Text())
    score = db.Integer(default=0)
    uploaded_time = db.Column(db.DateTime, default=datetime.now)
    approved_time = db.Column(db.DateTime, default=None)

    def approve(self):
        self.approved_time = datetime.now()
        self.store_confession()

    def store_confession(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Confession: %r>' % self.confession
