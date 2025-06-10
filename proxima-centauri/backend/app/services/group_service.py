from app.extensions import db
from app.models.group import Group

def create_group(data):
    group = Group(**data)
    db.session.add(group)
    db.session.commit()
    return group

def get_all_groups():
    return Group.query.all()

def get_group_by_id(group_id):
    return Group.query.get(group_id)

def update_group(group, data):
    for key, value in data.items():
        setattr(group, key, value)
    db.session.commit()
    return group

def delete_group(group):
    db.session.delete(group)
    db.session.commit()
