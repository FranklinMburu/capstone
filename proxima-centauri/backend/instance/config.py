import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'proxima.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET = 'your_super_secret_jwt_key'
