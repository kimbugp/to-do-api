import os

from flask import Flask
from flask_migrate import Migrate
from flask_restplus import Api, Resource

from api.models import db
from flask_marshmallow import Marshmallow

app= Flask(__name__)
api = Api(app)

def create_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] =os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
    db.init_app(app)
    migrate = Migrate(app, db)
    ma = Marshmallow(app)
    #models
    from api.models import User

    #views
    from api import views

    return app
