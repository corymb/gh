from flask import flash, render_template, redirect, request, url_for
from app import app, db

from app.models import Confession


@app.route('/')
def show_confessions():
    confessions = Confession.query.filter(Confession.approved_time !=
            None).order_by(Confession.approved_time.desc())
    return render_template('show_entries.html', confessions=confessions)


@app.route('/<confession_id>', methods=['GET', 'POST'])
def show_confession(confession_id):
    confession = Confession.query.get(confession_id)
    if request.method == 'POST':
        upvote = True if request.form.get('upvote') == '1' else False
        if upvote:
            confession.upvote()
        else:
            confession.downvote()
        return u'%s' % confession.score

    # Template re-use requires an iterable:
    confession = confession,
    return render_template('show_entries.html', confessions=confession)

@app.route('/add/', methods=['POST'])
def add_entry():
    confession = Confession(confession=request.form['confession'])
    confession.store_confession()
    flash('Your confession has been posted and is pending approval')
    return redirect(url_for('show_confessions'))


@app.route('/downvote/')
def upvote():
    pass


@app.route('/upvote/')
def downvote():
    pass
