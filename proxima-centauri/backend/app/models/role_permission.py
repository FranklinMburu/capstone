from sqlalchemy import Column, String, ForeignKey, Table
from app.extensions import db

role_permissions = db.Table(
    'role_permissions',
    db.Column('role_id', String, db.ForeignKey('roles.id'), primary_key=True),
    db.Column('permission_id', String, db.ForeignKey('permissions.id'), primary_key=True)
)
