from flask import Flask, request
from flask_restplus import Api, Resource
from api.serializer import UserSchema
import json
import jwt

from api.models import User, db
from main import api
from api.utils.token_header import token_header


@api.route('/')
class AuthResource(Resource):
    def post(self):
        userdata = UserSchema().load(request.get_json())
        if userdata.errors:
            return userdata.errors, 400
        user = User(**userdata.data)
        if not User.query.filter_by(username=userdata.data["username"]).count():
            db.session.add(user)
            db.session.commit()
        token = jwt.encode(
            {'username': userdata.data['username']}, 'andela', algorithm='HS256')
        return {'user': UserSchema().dump(user).data, 'token': token.decode('UTF-8')}, 201


@api.route('/<string:uname>')
class Home(Resource):
    @token_header
    def get(self, uname):
        user = User.query.filter_by(username=uname).first()
        usersdata = UserSchema().dump(user).data
        if usersdata:
            return usersdata, 200
        return {'message': 'no such user'}, 200

    @token_header
    def put(self, uname):
        user = User.query.filter_by(username=uname).first()
        update = UserSchema().dump(request.get_json())
        if update.errors:
            return update.errors, 400
        for key, value in update.data.items():
            setattr(user, key, value)
        db.session.commit()
        return UserSchema().dump(user).data

    @token_header
    def delete(self, uname):
        user = User.query.filter_by(username=uname).delete()
        db.session.commit()
        return {'message': 'user deleted'}
