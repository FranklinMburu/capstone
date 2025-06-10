from flask import Blueprint
from app.controllers.permission_controller import (
    create_permission_controller, get_permission_controller,
    list_permissions_controller, update_permission_controller,
    delete_permission_controller
)

permission_bp = Blueprint("permission", __name__, url_prefix="/permissions")

permission_bp.post("")(create_permission_controller)
permission_bp.get("")(list_permissions_controller)
permission_bp.get("/<permission_id>")(get_permission_controller)
permission_bp.put("/<permission_id>")(update_permission_controller)
permission_bp.delete("/<permission_id>")(delete_permission_controller)
