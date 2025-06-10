from app.models.user import User
from app.extensions import db
from app.utils.auth import hash_password, verify_password, generate_token

def create_user(data):
    user = User(
        full_name=data['full_name'],
        phone_number=data['phone_number'],
        email=data.get('email'),
        password_hash=hash_password(data['password']),
    )
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(phone_number, password):
    user = User.query.filter_by(phone_number=phone_number).first()
    if user and verify_password(password, user.password_hash):
        return generate_token(user.id), user
    return None, None

def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()

def get_user_by_phone_number(phone_number):
    return User.query.filter_by(phone_number=phone_number).first()