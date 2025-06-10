from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models.user import User

def require_role(role_name):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = User.query.filter_by(id=user_id).first()
            if not user:
                return jsonify({"msg": "User not found"}), 404
            roles = [role.name for role in user.roles]
            if role_name not in roles:
                return jsonify({"msg": "Access denied. Role '{}' required.".format(role_name)}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def require_permission(permission_name):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = User.query.filter_by(id=user_id).first()
            if not user:
                return jsonify({"msg": "User not found"}), 404

            # Gathers all permissions of the user's roles
            user_permissions = set()
            for role in user.roles:
                for perm in role.permissions:
                    user_permissions.add(perm.name)

            if permission_name not in user_permissions:
                return jsonify({"msg": "Access denied. Permission '{}' required.".format(permission_name)}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
