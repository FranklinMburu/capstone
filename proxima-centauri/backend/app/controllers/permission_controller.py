from flask import request, jsonify
from app.services.permission_service import (
    create_permission, get_permission_by_id,
    list_permissions, update_permission, delete_permission
)
from app.schemas.permission_schema import PermissionSchema

permission_schema = PermissionSchema()
permissions_schema = PermissionSchema(many=True)

def create_permission_controller():
    data = request.get_json()
    errors = permission_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    permission = create_permission(data)
    return jsonify(permission_schema.dump(permission)), 201

def get_permission_controller(permission_id):
    permission = get_permission_by_id(permission_id)
    if not permission:
        return jsonify({"error": "Permission not found"}), 404
    return jsonify(permission_schema.dump(permission))

def list_permissions_controller():
    permissions = list_permissions()
    return jsonify(permissions_schema.dump(permissions))

def update_permission_controller(permission_id):
    permission = get_permission_by_id(permission_id)
    if not permission:
        return jsonify({"error": "Permission not found"}), 404
    data = request.get_json()
    permission = update_permission(permission, data)
    return jsonify(permission_schema.dump(permission))

def delete_permission_controller(permission_id):
    permission = get_permission_by_id(permission_id)
    if not permission:
        return jsonify({"error": "Permission not found"}), 404
    delete_permission(permission)
    return jsonify({"message": "Permission deleted"}), 200
