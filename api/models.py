from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(36), unique=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(60))

    def __repr__(self):
        return '<User %r>' % self.username


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column (db.String(36),db.ForeignKey('user.id'))
    task = db.Column(db.String(36))
