from flask import Blueprint
from app.controllers.payment_method import (
    create_payment_method_controller,
    get_payment_methods_controller,
    get_payment_method_controller,
)

payment_method_bp = Blueprint("payment_method", __name__, url_prefix="/payment_methods")

payment_method_bp.post("")(create_payment_method_controller)
payment_method_bp.get("/user/<user_id>")(get_payment_methods_controller)
payment_method_bp.get("/<pm_id>")(get_payment_method_controller)
