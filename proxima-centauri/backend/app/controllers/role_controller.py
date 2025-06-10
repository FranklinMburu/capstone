from flask import request, jsonify, Blueprint
from app.services.role_service import (
    create_role, get_role_by_id,
    list_roles, update_role, delete_role
)
from app.services.permission_service import get_permission_by_id  # import needed
from app.schemas.role_schema import RoleSchema
from app.extensions import db  # for db.session commit

role_bp = Blueprint('role_bp', __name__, url_prefix='/roles')

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

# Existing CRUD endpoints
@role_bp.route('', methods=['POST'])
def create_role_controller():
    data = request.get_json()
    errors = role_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    role = create_role(data)
    return jsonify(role_schema.dump(role)), 201

@role_bp.route('/<role_id>', methods=['GET'])
def get_role_controller(role_id):
    role = get_role_by_id(role_id)
    if not role:
        return jsonify({"error": "Role not found"}), 404
    return jsonify(role_schema.dump(role))

@role_bp.route('', methods=['GET'])
def list_roles_controller():
    roles = list_roles()
    return jsonify(roles_schema.dump(roles))

@role_bp.route('/<role_id>', methods=['PUT'])
def update_role_controller(role_id):
    role = get_role_by_id(role_id)
    if not role:
        return jsonify({"error": "Role not found"}), 404
    data = request.get_json()
    role = update_role(role, data)
    return jsonify(role_schema.dump(role))

@role_bp.route('/<role_id>', methods=['DELETE'])
def delete_role_controller(role_id):
    role = get_role_by_id(role_id)
    if not role:
        return jsonify({"error": "Role not found"}), 404
    delete_role(role)
    return jsonify({"message": "Role deleted"}), 200

# NEW endpoint: Assign Permission to Role
@role_bp.route('/<role_id>/permissions', methods=['POST'])
def assign_permission_to_role(role_id):
    role = get_role_by_id(role_id)
    if not role:
        return jsonify({"msg": "Role not found"}), 404

    data = request.get_json()
    permission_id = data.get('permission_id')
    if not permission_id:
        return jsonify({"msg": "permission_id is required"}), 400

    permission = get_permission_by_id(permission_id)
    if not permission:
        return jsonify({"msg": "Permission not found"}), 404

    if permission in role.permissions:
        return jsonify({"msg": "Permission already assigned to role"}), 409

    role.permissions.append(permission)
    db.session.commit()

    return jsonify({"msg": f"Permission '{permission.name}' assigned to role '{role.name}'"}), 200
