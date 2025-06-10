from sqlalchemy import Column, String, ForeignKey, Table
from app.extensions import db

user_roles = db.Table(
    'user_roles',
    db.Column('user_id', String, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', String, db.ForeignKey('roles.id'), primary_key=True)
)
