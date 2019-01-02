from functools import wraps
from flask import request
import jwt


def token_header(f):
    ''' Function to get the token using the header'''
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        
        if not token:
            return {'message': 'No auth token'}, 401
        try:
            data = jwt.decode(token, 'andela', algorithms=['HS256'])
        except:
            return {'message': 'Invalid token'}, 401
        return f(*args, **kwargs)

    return decorated
