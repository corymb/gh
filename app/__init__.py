from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('../settings/common.py')

db = SQLAlchemy(app)


import views
