from app.extensions import db
from app.models.group_membership import GroupMembership

def add_member(data):
    membership = GroupMembership(**data)
    db.session.add(membership)
    db.session.commit()
    return membership

def get_all_memberships():
    return GroupMembership.query.all()

def get_membership_by_id(membership_id):
    return GroupMembership.query.get(membership_id)

def remove_member(membership):
    db.session.delete(membership)
    db.session.commit()
