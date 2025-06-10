from flask import Blueprint
from app.controllers.notification import (
    create_notification_controller, get_notification_controller,
    list_notifications_controller, update_notification_controller,
    delete_notification_controller
)

notification_bp = Blueprint("notification", __name__, url_prefix="/notifications")

notification_bp.post("")(create_notification_controller)
notification_bp.get("")(list_notifications_controller)
notification_bp.get("/<notification_id>")(get_notification_controller)
notification_bp.put("/<notification_id>")(update_notification_controller)
notification_bp.delete("/<notification_id>")(delete_notification_controller)
