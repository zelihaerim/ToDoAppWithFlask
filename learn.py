
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Zeliha/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

"""
sqlite3
.tables
.exit
python
db.create_all()
exit()
python
>>> from todo import db,User
>>> admin = User(username='admin', email='admin@example.com')
>>> db.session.add(admin)
>>> db.session.commit()
>>> exit()
"""
