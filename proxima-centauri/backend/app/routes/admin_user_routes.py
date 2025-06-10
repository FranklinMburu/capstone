from flask import Blueprint
from app.controllers.admin_user_controller import (
    create_admin_user_controller, get_admin_user_controller,
    list_admin_users_controller, update_admin_user_controller,
    delete_admin_user_controller
)

admin_user_bp = Blueprint("admin_user", __name__, url_prefix="/admin-users")

admin_user_bp.post("")(create_admin_user_controller)
admin_user_bp.get("")(list_admin_users_controller)
admin_user_bp.get("/<admin_id>")(get_admin_user_controller)
admin_user_bp.put("/<admin_id>")(update_admin_user_controller)
admin_user_bp.delete("/<admin_id>")(delete_admin_user_controller)
