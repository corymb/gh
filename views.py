from flask import flash, render_template, redirect, request, url_for
from app import app, db

from app.models import Confession


@app.route('/')
def show_entries():
    confessions = Confession.query.filter(Confession.approved_time !=
            None).order_by(Confession.approved_time.desc())
    return render_template('show_entries.html', confessions=confessions)


@app.route('/add/', methods=['POST'])
def add_entry():
    confession = Confession(confession=request.form['confession'])
    confession.store_confession()
    flash('Your confession has been posted and is pending approval')
    return redirect(url_for('show_entries'))


@app.route('/downvote/')
def upvote():
    pass


@app.route('/upvote/')
def downvote():
    pass
