from app.models.permission import Permission
from app.extensions import db

def create_permission(data):
    permission = Permission(**data)
    db.session.add(permission)
    db.session.commit()
    return permission

def get_permission_by_id(permission_id):
    return Permission.query.get(permission_id)

def list_permissions():
    return Permission.query.all()

def update_permission(permission, data):
    for key, value in data.items():
        setattr(permission, key, value)
    db.session.commit()
    return permission

def delete_permission(permission):
    db.session.delete(permission)
    db.session.commit()
