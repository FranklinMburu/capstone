import uuid
from flask import request, jsonify
from app.extensions import db
from app.models.group_role import GroupRole
from app.schemas.group_role_schema import GroupRoleSchema

group_role_schema = GroupRoleSchema()
group_roles_schema = GroupRoleSchema(many=True)

def create_group_role():
    data = request.get_json()
    errors = group_role_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    group_role = GroupRole(
        id=str(uuid.uuid4()),
        group_id=data['group_id'],
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(group_role)
    db.session.commit()
    return group_role_schema.jsonify(group_role), 201

def get_group_roles():
    roles = GroupRole.query.all()
    return group_roles_schema.jsonify(roles), 200

def get_group_role(role_id):
    role = GroupRole.query.get(role_id)
    if not role:
        return jsonify({'message': 'Role not found'}), 404
    return group_role_schema.jsonify(role), 200

def update_group_role(role_id):
    role = GroupRole.query.get(role_id)
    if not role:
        return jsonify({'message': 'Role not found'}), 404

    data = request.get_json()
    errors = group_role_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400

    if 'name' in data:
        role.name = data['name']
    if 'description' in data:
        role.description = data['description']

    db.session.commit()
    return group_role_schema.jsonify(role), 200

def delete_group_role(role_id):
    role = GroupRole.query.get(role_id)
    if not role:
        return jsonify({'message': 'Role not found'}), 404

    db.session.delete(role)
    db.session.commit()
    return jsonify({'message': 'Role deleted'}), 200
