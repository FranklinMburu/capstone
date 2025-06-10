from flask import Blueprint, request, jsonify
from app.schemas.group_role_schema import GroupRoleSchema
from app.services.group_role_service import create_group_role, get_all_group_roles, get_group_role_by_id, update_group_role, delete_group_role

group_role_bp = Blueprint('group_role_bp', __name__, url_prefix='/group-roles')
role_schema = GroupRoleSchema()
roles_schema = GroupRoleSchema(many=True)

@group_role_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    errors = role_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    role = create_group_role(data)
    return role_schema.jsonify(role), 201

@group_role_bp.route('', methods=['GET'])
def get_all():
    roles = get_all_group_roles()
    return roles_schema.jsonify(roles), 200

@group_role_bp.route('/<int:role_id>', methods=['GET'])
def get_one(role_id):
    role = get_group_role_by_id(role_id)
    if not role:
        return jsonify({"message": "Role not found"}), 404
    return role_schema.jsonify(role), 200

@group_role_bp.route('/<int:role_id>', methods=['PUT'])
def update(role_id):
    role = get_group_role_by_id(role_id)
    if not role:
        return jsonify({"message": "Role not found"}), 404
    data = request.get_json()
    errors = role_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    updated_role = update_group_role(role, data)
    return role_schema.jsonify(updated_role), 200

@group_role_bp.route('/<int:role_id>', methods=['DELETE'])
def delete(role_id):
    role = get_group_role_by_id(role_id)
    if not role:
        return jsonify({"message": "Role not found"}), 404
    delete_group_role(role)
    return jsonify({"message": "Role deleted"}), 200
