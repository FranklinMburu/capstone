from flask import Blueprint
from app.controllers.role_controller import (
    create_role_controller, get_role_controller,
    list_roles_controller, update_role_controller,
    delete_role_controller
)

role_bp = Blueprint("role", __name__, url_prefix="/roles")

role_bp.post("")(create_role_controller)
role_bp.get("")(list_roles_controller)
role_bp.get("/<role_id>")(get_role_controller)
role_bp.put("/<role_id>")(update_role_controller)
role_bp.delete("/<role_id>")(delete_role_controller)
