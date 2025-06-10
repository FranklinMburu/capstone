import uuid
from flask import request, jsonify
from app.extensions import db
from app.models.group_membership import GroupMembership
from app.schemas.group_membership_schema import GroupMembershipSchema

membership_schema = GroupMembershipSchema()
memberships_schema = GroupMembershipSchema(many=True)

def add_member():
    data = request.get_json()
    errors = membership_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    membership = GroupMembership(
        id=str(uuid.uuid4()),
        user_id=data['user_id'],
        group_id=data['group_id']
    )
    db.session.add(membership)
    db.session.commit()
    return membership_schema.jsonify(membership), 201

def get_memberships():
    memberships = GroupMembership.query.all()
    return memberships_schema.jsonify(memberships), 200

def get_membership(membership_id):
    membership = GroupMembership.query.get(membership_id)
    if not membership:
        return jsonify({'message': 'Membership not found'}), 404
    return membership_schema.jsonify(membership), 200

def remove_member(membership_id):
    membership = GroupMembership.query.get(membership_id)
    if not membership:
        return jsonify({'message': 'Membership not found'}), 404

    db.session.delete(membership)
    db.session.commit()
    return jsonify({'message': 'Member removed from group'}), 200
