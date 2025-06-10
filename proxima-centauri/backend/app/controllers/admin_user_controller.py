from flask import request, jsonify
from app.services.admin_user_service import (
    create_admin_user, get_admin_user_by_id,
    list_admin_users, update_admin_user, delete_admin_user
)
from app.schemas.admin_user_schema import AdminUserSchema

admin_user_schema = AdminUserSchema()
admin_users_schema = AdminUserSchema(many=True)

def create_admin_user_controller():
    data = request.get_json()
    errors = admin_user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    admin_user = create_admin_user(data)
    return jsonify(admin_user_schema.dump(admin_user)), 201

def get_admin_user_controller(admin_id):
    admin_user = get_admin_user_by_id(admin_id)
    if not admin_user:
        return jsonify({"error": "Admin user not found"}), 404
    return jsonify(admin_user_schema.dump(admin_user))

def list_admin_users_controller():
    admin_users = list_admin_users()
    return jsonify(admin_users_schema.dump(admin_users))

def update_admin_user_controller(admin_id):
    admin_user = get_admin_user_by_id(admin_id)
    if not admin_user:
        return jsonify({"error": "Admin user not found"}), 404
    data = request.get_json()
    admin_user = update_admin_user(admin_user, data)
    return jsonify(admin_user_schema.dump(admin_user))

def delete_admin_user_controller(admin_id):
    admin_user = get_admin_user_by_id(admin_id)
    if not admin_user:
        return jsonify({"error": "Admin user not found"}), 404
    delete_admin_user(admin_user)
    return jsonify({"message": "Admin user deleted"}), 200
