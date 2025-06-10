from app.extensions import db
from app.models.group_role import GroupRole

def create_group_role(data):
    role = GroupRole(**data)
    db.session.add(role)
    db.session.commit()
    return role

def get_all_group_roles():
    return GroupRole.query.all()

def get_group_role_by_id(role_id):
    return GroupRole.query.get(role_id)

def update_group_role(role, data):
    for key, value in data.items():
        setattr(role, key, value)
    db.session.commit()
    return role

def delete_group_role(role):
    db.session.delete(role)
    db.session.commit()
