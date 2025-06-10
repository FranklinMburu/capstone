import uuid
from flask import request, jsonify
from app.extensions import db
from app.models.group import Group
from app.schemas.group_schema import GroupSchema

group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

def create_group():
    data = request.get_json()
    errors = group_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    group = Group(
        id=str(uuid.uuid4()),
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(group)
    db.session.commit()
    return group_schema.jsonify(group), 201

def get_groups():
    groups = Group.query.all()
    return groups_schema.jsonify(groups), 200

def get_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'message': 'Group not found'}), 404
    return group_schema.jsonify(group), 200

def update_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'message': 'Group not found'}), 404

    data = request.get_json()
    errors = group_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400

    if 'name' in data:
        group.name = data['name']
    if 'description' in data:
        group.description = data['description']

    db.session.commit()
    return group_schema.jsonify(group), 200

def delete_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'message': 'Group not found'}), 404

    db.session.delete(group)
    db.session.commit()
    return jsonify({'message': 'Group deleted'}), 200
