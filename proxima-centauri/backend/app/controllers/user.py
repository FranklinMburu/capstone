from flask import request, jsonify
from app.schemas.user import UserCreateSchema, UserLoginSchema, UserResponseSchema
from app.services.user import create_user, authenticate_user

create_schema = UserCreateSchema()
login_schema = UserLoginSchema()
response_schema = UserResponseSchema()

def register_user():
    data = create_schema.load(request.json)
    user = create_user(data)
    return jsonify(response_schema.dump(user)), 201

def login_user():
    data = login_schema.load(request.json)
    token, user = authenticate_user(data['phone_number'], data['password'])
    if user:
        return jsonify({
            "token": token,
            "user": response_schema.dump(user)
        }), 200
    return jsonify({"message": "Invalid credentials"}), 401
