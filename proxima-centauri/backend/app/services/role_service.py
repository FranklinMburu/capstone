from app.models.role import Role
from app.extensions import db

def create_role(data):
    role = Role(**data)
    db.session.add(role)
    db.session.commit()
    return role

def get_role_by_id(role_id):
    return Role.query.get(role_id)

def list_roles():
    return Role.query.all()

def update_role(role, data):
    for key, value in data.items():
        setattr(role, key, value)
    db.session.commit()
    return role

def delete_role(role):
    db.session.delete(role)
    db.session.commit()
