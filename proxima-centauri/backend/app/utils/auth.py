import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed):
    return check_password_hash(hashed, password)

def generate_token(user_id):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(),
        "sub": user_id
    }
    return jwt.encode(payload, current_app.config['JWT_SECRET'], algorithm="HS256")

def decode_token(token):
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=["HS256"])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
