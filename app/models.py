from datetime import datetime

from app import db


class Confession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    confession = db.Column(db.Text())
    score = db.Column(db.Integer(default=1))
    uploaded_time = db.Column(db.DateTime, default=datetime.now)
    approved_time = db.Column(db.DateTime, default=None)

    def __init__(self, *args, **kwargs):
        """
        SQLAlchemy only populates default values with INSERT and UPDATE, so you
        have to manually set the starting score:
        """
        if 'score' not in kwargs:
             kwargs['score'] = 1
        super(Confession, self).__init__(**kwargs)

    def approve(self):
        self.approved_time = datetime.now()
        self.store_confession()

    def store_confession(self):
        db.session.add(self)
        db.session.commit()

    def upvote(self):
        self.score += 1
        self.store_confession()

    def downvote(self):
        self.score -= 1
        self.store_confession()

    def __repr__(self):
        return '<Confession: %r>' % self.confession
