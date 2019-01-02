from marshmallow import Schema, ValidationError, fields, post_load
from werkzeug.security import check_password_hash, generate_password_hash

from api.models import User


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(load_only=True, required=True)

    @post_load
    def returned_data(self, data):
        if data.get('password'):
            pw_hash = generate_password_hash(data.get('password'))
            data['password'] = pw_hash
        return data
