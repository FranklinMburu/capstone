# 🧠 Human Reasoning Behind Users Entity Creation (Proxima Centauri)

This document walks through the creation of the `Users` entity in your Proxima Centauri Flask application. It explains **how**, **why**, and **what breaks** if parts are missing, from a human reasoning perspective.

---

## ✅ 1. Model → `backend/app/models/user.py`

### Why we wrote this

We need a persistent representation of a User in the database. SQLAlchemy provides an ORM for this.

### Line-by-line Reasoning

```python
from datetime import datetime         # Tracks when the user was created
from uuid import uuid4               # Generates a unique ID for each user
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.sqlite import BLOB
from app.extensions import db         # SQLAlchemy instance (shared across app)

def generate_uuid():
    return str(uuid4())              # Guarantees UUID as default user ID

class User(db.Model):
    __tablename__ = 'users'          # Explicit table name for clarity

    id = Column(String, primary_key=True, default=generate_uuid)  # Primary key
    full_name = Column(String(120), nullable=False)               # Mandatory name
    phone_number = Column(String(20), unique=True, nullable=False) # Acts as login ID
    email = Column(String(120), unique=True, nullable=True)       # Optional but unique
    password_hash = Column(String(128), nullable=False)           # Secured password
    is_verified = Column(Boolean, default=False)                  # Track phone/email verification
    created_at = Column(DateTime, default=datetime.utcnow)        # Track registration timestamp
```

### Why we need it:

* It defines what a User *is*.
* It's required for database creation and user registration logic.

### What breaks if missing:

* No users table in DB → registration, login, JWT will fail.

---

## ✅ 2. Schema → `backend/app/schemas/user.py`

### Why we wrote this

To **validate** input and **serialize** output for API endpoints using Marshmallow.

### Schema logic

```python
class UserCreateSchema(Schema):         # Input schema for registration
    full_name = fields.String(required=True)
    phone_number = fields.String(required=True)
    email = fields.Email(required=False)
    password = fields.String(required=True)

class UserLoginSchema(Schema):          # Input schema for login
    phone_number = fields.String(required=True)
    password = fields.String(required=True)

class UserResponseSchema(Schema):       # Output schema after login/register
    id = fields.String()
    full_name = fields.String()
    phone_number = fields.String()
    email = fields.Email()
    is_verified = fields.Boolean()
    created_at = fields.DateTime()
```

### What breaks if missing:

* API input will not be validated.
* Response formatting will be inconsistent.

---

## ✅ 3. Auth Utility → `backend/app/utils/auth.py`

### Why we wrote this

Centralized logic to handle:

* Hashing passwords (secure storage)
* Verifying passwords (secure login)
* JWT token generation and decoding (authentication)

```python
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

# Hash the user password

def hash_password(password):
    return generate_password_hash(password)

# Compare stored and input passwords

def verify_password(password, hashed):
    return check_password_hash(hashed, password)

# Encode a JWT token for session/login

def generate_token(user_id):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(),
        "sub": user_id
    }
    return jwt.encode(payload, current_app.config['JWT_SECRET'], algorithm="HS256")

# Decode token and extract user

def decode_token(token):
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=["HS256"])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
```

### What breaks if missing:

* Passwords are stored in plaintext (security risk)
* JWT auth system won't work → No login, no protected routes

---

## ✅ 4. Service → `backend/app/services/user_service.py`

### Why we wrote this

* Encapsulates business logic.
* Keeps controllers clean.

```python
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
```

### What breaks if missing:

* No way to create or log in users
* Logic will have to be duplicated in controllers → bad design

---

## ✅ 5. Controller → `backend/app/controllers/user_controller.py`

### Why we wrote this

* Bridges request input → service → response output

```python
from flask import request, jsonify
from app.schemas.user import UserCreateSchema, UserLoginSchema, UserResponseSchema
from app.services.user_service import create_user, authenticate_user

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
```

### What breaks if missing:

* API has no entry point for `/register` or `/login`

---

## ✅ 6. Route → `backend/app/routes/user_routes.py`

### Why we wrote this

* Connects URL paths to controller functions

```python
from flask import Blueprint
from app.controllers.user_controller import register_user, login_user

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')

user_bp.route('/register', methods=['POST'])(register_user)
user_bp.route('/login', methods=['POST'])(login_user)
```

### What breaks if missing:

* Flask won’t know what to do with `/api/users/register` or `/login`

---

## ✅ 7. App Setup → `run.py`

### Why we wrote this

* Initializes Flask app
* Registers extensions, routes
* Runs the server

```python
from flask import Flask
from app.extensions import db
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('instance/config.py')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```

### What breaks if missing:

* No app will run
* No blueprints loaded → routes dead
* No database tables initialized

---

## ✅ 8. Config → `backend/instance/config.py`

### Why we wrote this

* Store environment-based app settings

```python
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'proxima.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET = 'your_super_secret_jwt_key'
```

### What breaks if missing:

* DB and JWT token logic won’t work
* App will crash on startup

---

## ✅ 9. Extensions → `backend/app/extensions.py`

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### Why we wrote this

* Central place to initialize extensions like `db`
* Avoids circular imports

### What breaks if missing:

* `db` won't be initialized or used in models or services

---

## ✅ 10. Alembic Setup

### Why we wrote this

* Version control for schema (users table)
* Apply migrations instead of deleting/recreating DB

### Commands

```bash
alembic init migrations
# Set DB in alembic.ini → sqlite:///instance/proxima.db
# Set target_metadata in env.py
alembic revision --autogenerate -m "Create users table"
alembic upgrade head
```

### What breaks if missing:

* Cannot track schema changes
* Manual DB edits prone to error

---

## 🧪 Final Testing: cURL or Postman

### Register:

```bash
curl -X POST http://127.0.0.1:5000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"full_name": "Alice", "phone_number": "0712345678", "email": "alice@example.com", "password": "pass123"}'
```

### Login:

```bash
curl -X POST http://127.0.0.1:5000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "0712345678", "password": "pass123"}'
```

---

## Summary

Each piece of this stack is essential:

* **Model** defines structure
* **Schema** validates/serializes data
* **Auth Utility** secures data
* **Service** runs logic
* **Controller** connects API input/output
* **Routes** connect endpoints
* **App** initializes everything
* **Config** stores sensitive data
* **Extensions** enable modularity
* **Alembic** ensures migration history

Together, they give us a robust, scalable, secure foundation for user auth in Proxima Centauri.












REMEMBER TO CHANGE THE JWT_SECRET LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  !!!!!!!!!!!!!!!!!!!!!!!!!!


i did this setting too 
python.analysis.typeCheckingMode













