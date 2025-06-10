from flask import request, jsonify, Blueprint
from app.services.user import get_user_by_id
from app.services.role_service import get_role_by_id
from app.extensions import db

user_role_bp = Blueprint('user_role_bp', __name__, url_prefix='/users')

@user_role_bp.route('/<user_id>/roles', methods=['POST'])
def assign_role_to_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    data = request.get_json()
    role_id = data.get('role_id')
    if not role_id:
        return jsonify({"msg": "role_id is required"}), 400

    role = get_role_by_id(role_id)
    if not role:
        return jsonify({"msg": "Role not found"}), 404

    if role in user.roles:
        return jsonify({"msg": "Role already assigned to user"}), 409

    user.roles.append(role)
    db.session.commit()

    return jsonify({"msg": f"Role '{role.name}' assigned to user '{user.full_name}'"}), 200
